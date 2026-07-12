/**
 * Decodificador Hexadecimal ultra-optimizado de memoria plana.
 * Convierte strings Hex a Uint8Array sin instanciaciones redundantes.
 */
function hexToUint8Array(hexString) {
  if (hexString.length % 2 !== 0) {
    throw new Error("Longitud hexadecimal no alineada.");
  }
  const numBytes = hexString.length / 2;
  const array = new Uint8Array(numBytes);
  for (let i = 0; i < numBytes; i++) {
    const byte = parseInt(hexString.substring(i * 2, i * 2 + 2), 16);
    if (isNaN(byte)) {
      throw new Error("Carácter hexadecimal inválido.");
    }
    array[i] = byte;
  }
  return array;
}

export default {
  async fetch(request, env) {
    // Encapsulación global para garantizar inmunidad frente a caídas de infraestructura
    try {
      const signatureHex = request.headers.get("X-Signature");
      const timestampStr = request.headers.get("X-Timestamp");

      // --- FILTRO 1: Credenciales ausentes (HTTP 401 Unauthorized) ---
      if (!signatureHex || !timestampStr) {
        return new Response("Faltan credenciales criptográficas de acceso", {
          status: 401,
          headers: { "Content-Type": "text/plain; charset=UTF-8" }
        });
      }

      // --- FILTRO 2: Validación estructural previa (HTTP 400 Bad Request) ---
      // Una firma Ed25519 en formato hexadecimal debe medir exactamente 128 caracteres (64 bytes)
      if (signatureHex.length !== 128) {
        return new Response("Acceso Denegado: Estructura de firma malformada", {
          status: 400,
          headers: { "Content-Type": "text/plain; charset=UTF-8" }
        });
      }

      // --- FILTRO 3: Defensa de ventana temporal / Anti-Replay (HTTP 403 Forbidden) ---
      const requestTimestamp = parseInt(timestampStr, 10);
      const currentTimestamp = Math.floor(Date.now() / 1000); // Tiempo del nodo Edge en segundos
      
      if (isNaN(requestTimestamp) || Math.abs(currentTimestamp - requestTimestamp) > 300) {
        return new Response("Acceso Denegado: Ventana de tiempo inválida o expirada", {
          status: 403,
          headers: { "Content-Type": "text/plain; charset=UTF-8" }
        });
      }

      // --- FILTRO 4: Verificación interna de configuración de entorno ---
      if (!env.PUBLIC_KEY_HEX) {
        return new Response("Error de infraestructura: Clave perimetral no inyectada", {
          status: 500,
          headers: { "Content-Type": "text/plain; charset=UTF-8" }
        });
      }

      // --- FILTRO 5: Parseo seguro de Buffers (Previene excepciones crudas) ---
      let publicKeyBuffer, signatureBuffer, dataToVerify;
      try {
        publicKeyBuffer = hexToUint8Array(env.PUBLIC_KEY_HEX.trim());
        signatureBuffer = hexToUint8Array(signatureHex);
        
        // Estructura del Payload firmado (en este diseño: el string del timestamp)
        const encoder = new TextEncoder();
        dataToVerify = encoder.encode(timestampStr);
      } catch (parseError) {
        // Captura cualquier fallo si el atacante envía strings con caracteres inválidos no-hex
        return new Response("Acceso Denegado: Codificación criptográfica corrupta", {
          status: 403,
          headers: { "Content-Type": "text/plain; charset=UTF-8" }
        });
      }

      // --- FILTRO 6: Importación y Ejecución en Web Crypto API ---
      let cryptoKey;
      try {
        cryptoKey = await crypto.subtle.importKey(
          "raw",
          publicKeyBuffer,
          { name: "Ed25519", namedCurve: "Ed25519" },
          false,
          ["verify"]
        );
      } catch (importError) {
        // Evita el error 500 si la clave pública configurada en el secreto estuviera corrupta
        return new Response("Error de infraestructura: Clave perimetral inválida", {
          status: 500,
          headers: { "Content-Type": "text/plain; charset=UTF-8" }
        });
      }

      // Verificación matemática estricta
      let isAuthentic = false;
      try {
        isAuthentic = await crypto.subtle.verify(
          { name: "Ed25519" },
          cryptoKey,
          signatureBuffer,
          dataToVerify
        );
      } catch (cryptoVerifyError) {
        // Captura desviaciones matemáticas internas del motor de verificación
        return new Response("Acceso Denegado: Error de validación en operaciones de firma", {
          status: 403,
          headers: { "Content-Type": "text/plain; charset=UTF-8" }
        });
      }

      // --- FILTRO 7: Evaluación del Resultado de Autenticidad ---
      if (!isAuthentic) {
        return new Response("Acceso Denegado: Autenticidad de firma no válida", {
          status: 403,
          headers: { "Content-Type": "text/plain; charset=UTF-8" }
        });
      }

      // --- PASO DE ÉXITO DEFINITIVO (HTTP 200 OK) ---
      return new Response("Verificación Exitosa: Integridad y Veracidad Confirmada", {
        status: 200,
        headers: { "Content-Type": "text/plain; charset=UTF-8" }
      });

    } catch (globalCriticalError) {
      // Muro de contención final insuperable
      return new Response("Error interno crítico del validador edge", {
        status: 500,
        headers: { "Content-Type": "text/plain; charset=UTF-8" }
      });
    }
  }
};
