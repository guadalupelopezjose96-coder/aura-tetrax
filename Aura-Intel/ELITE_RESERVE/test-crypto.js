/* * PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
 * PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
 * MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
 * ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
 */

const { encrypt, decrypt } = require('./src/services/encryption.service');

const LLAVE_MAESTRA = "secreto-super-mega-ultra-secreto-96";
const MENSAJE_ORIGINAL = "Este es un secreto de Aura Intel que nadie debe ver.";

console.log("🛡️ Iniciando Cifrado Profundo...");
const paqueteCifrado = encrypt(MENSAJE_ORIGINAL, LLAVE_MAESTRA);

console.log("\n📁 Lo que se guardaría en la Base de Datos:");
console.log("--------------------------------------------");
console.log(paqueteCifrado);
console.log("--------------------------------------------");

console.log("\n🔓 Intentando descifrar...");
const recuperado = decrypt(paqueteCifrado, LLAVE_MAESTRA);

if (recuperado === MENSAJE_ORIGINAL) {
  console.log("✅ RESULTADO: El mensaje fue recuperado íntegro.");
  console.log("💬 Mensaje: " + recuperado);
} else {
  console.log("❌ RESULTADO: Error en el cifrado.");
}
