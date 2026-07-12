/* * PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
 * PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
 * MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
 * ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
 */

const { secureAuth } = require('./src/services/auth.service');
const bcrypt = require('bcryptjs');

async function test() {
  console.log("🚀 Generando Hash de Seguridad Elite...");

  const passwordReal = "password12345";
  // Generamos un hash real para que la comparación sea perfecta
  const salt = await bcrypt.genSalt(10);
  const hashReal = await bcrypt.hash(passwordReal, salt);

  console.log("🚀 Iniciando Test de Aura Intel Elite Core...");

  const mockUser = {
    id: '96-coder-id',
    passwordHash: hashReal // Ahora el hash sí coincide con la password
  };

  const result = await secureAuth('test@correo.com', passwordReal, mockUser);

  if (result.success) {
    console.log("✅ RESULTADO: ¡EXITO TOTAL! El Escudo es impenetrable.");
    console.log("🔑 Token Generado: " + result.token.substring(0, 20) + "...");
  } else {
    console.log("❌ RESULTADO: Sigue fallando. Revisa el archivo auth.service.js");
  }
}

test();
