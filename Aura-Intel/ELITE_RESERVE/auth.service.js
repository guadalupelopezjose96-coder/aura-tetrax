/* * PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
 * PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
 * MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
 * ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
 */

// Importamos las herramientas de blindaje
const argon2 = require('argon2');
const { z } = require('zod');
const jwt = require('jsonwebtoken');
require('dotenv').config(); // Esto carga tus secretos del archivo .env

// 🛡️ ESQUEMA DE VALIDACIÓN (El filtro de Aura Intel)
const UserSchema = z.object({
  email: z.string().email().max(100),
  password: z.string().min(12).max(128),
});

/**
 * Servicio de Autenticación Elite Core
 */
const secureAuth = async (inputEmail, inputPassword, dbUser) => {
  try {
    // 1. Validar que la entrada no sea maliciosa
    const data = UserSchema.parse({ email: inputEmail, password: inputPassword });

    if (!dbUser) throw new Error('Usuario no encontrado');

    // 2. Verificar la contraseña con Argon2 (Máxima seguridad)
    const isMatch = await argon2.verify(dbUser.passwordHash, data.password);
    if (!isMatch) throw new Error('Credenciales incorrectas');

    // 3. Generar el Token de acceso (JWT)
    const token = jwt.sign(
      { id: dbUser.id, role: dbUser.role },
      process.env.JWT_SECRET, // Secreto guardado en tu .env
      { expiresIn: '15m' }    // Expira rápido para evitar robos
    );

    return { success: true, token };

  } catch (error) {
    // Registramos el error internamente, pero no le decimos al usuario por qué falló
    console.error("[SEGURIDAD]: Intento de acceso fallido mapeado.");
    return { success: false, message: "Error de autenticación" };
  }
};

// Exportamos la función para que otros archivos la usen
module.exports = { secureAuth };

