// src/index.ts
// Decodificador Hexadecimal ultra-optimizado de memoria plana.
function hexToUint8Array(hexString: string): Uint8Array {
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
    async fetch(request: Request, env: any) {
        try {
            const signatureHex = request.headers.get("X-Signature");
            const timestampStr = request.headers.get("X-Timestamp");

            // --- DEPURACIÓN: Logs solicitados ---
            console.log("Firma recibida:", signatureHex);
            console.log("Timestamp recibido:", timestampStr);

            // FILTRO 1: Credenciales ausentes
            if (!signatureHex || !timestampStr) {
                return new Response("Faltan credenciales", { status: 401 });
            }

            // FILTRO 2: Validación estructural (Ed25519 requiere 128 hex = 64 bytes)
            if (signatureHex.length !== 128) {
                return new Response("Acceso Denegado: Estructura de firma malformada", { status: 400 });
            }

            // FILTRO 3: Anti-Replay
            const requestTimestamp = parseInt(timestampStr, 10);
            const currentTimestamp = Math.floor(Date.now() / 1000);
            if (isNaN(requestTimestamp) || Math.abs(currentTimestamp - requestTimestamp) > 300) {
                return new Response("Acceso Denegado: Ventana de tiempo inválida", { status: 403 });
            }

            // FILTRO 4: Configuración de entorno
            if (!env.PUBLIC_KEY_HEX) {
                return new Response("Error de infraestructura: Clave no inyectada", { status: 500 });
            }

            // FILTRO 5: Parseo seguro
            let publicKeyBuffer, signatureBuffer, dataToVerify;
            try {
                publicKeyBuffer = hexToUint8Array(env.PUBLIC_KEY_HEX.trim());
                signatureBuffer = hexToUint8Array(signatureHex);
                const encoder = new TextEncoder();
                dataToVerify = encoder.encode(timestampStr); // Asegúrate que tu script firme solo el timestamp o el payload completo
            } catch (parseError) {
                return new Response("Acceso Denegado: Codificación corrupta", { status: 403 });
            }

            // FILTRO 6: Verificación Web Crypto API (Ed25519)
            const cryptoKey = await crypto.subtle.importKey(
                "raw",
                publicKeyBuffer,
                { name: "Ed25519", namedCurve: "Ed25519" },
                false,
                ["verify"]
            );

            const isAuthentic = await crypto.subtle.verify(
                { name: "Ed25519" },
                cryptoKey,
                signatureBuffer,
                dataToVerify
            );

            // FILTRO 7: Resultado
            if (!isAuthentic) {
                return new Response("Acceso Denegado: Firma no válida", { status: 403 });
            }

            return new Response("Verificación Exitosa: Integridad Confirmada", { status: 200 });

        } catch (globalCriticalError) {
            return new Response("Error interno crítico", { status: 500 });
        }
    }
}
