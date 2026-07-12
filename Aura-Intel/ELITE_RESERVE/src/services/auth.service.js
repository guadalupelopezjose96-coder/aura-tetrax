/* * PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
 * PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
 * MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
 * ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
 */

const bcrypt = require('bcryptjs'); // Cambio clave para Termux
const { z } = require('zod');
const jwt = require('jsonwebtoken');
require('dotenv').config();

const UserSchema = z.object({
  email: z.string().email().max(100),
  password: z.string().min(12).max(128),
});

const secureAuth = async (inputEmail, inputPassword, dbUser) => {
  try {
    const data = UserSchema.parse({ email: inputEmail, password: inputPassword });

    if (!dbUser) throw new Error('No user');

    // Usamos bcryptjs que no requiere permisos de compilación en Android
    const isMatch = await bcrypt.compare(data.password, dbUser.passwordHash);
    
    if (!isMatch) throw new Error('Invalid');

    const token = jwt.sign(
      { id: dbUser.id },
      process.env.JWT_SECRET || 'llave_temporal_de_emergencia',
      { expiresIn: '15m' }
    );

    return { success: true, token };

  } catch (error) {
    console.error("[AURA-ALERT]: Fallo detectado.");
    return { success: false, message: "Error de acceso" };
  }
};

module.exports = { secureAuth };
