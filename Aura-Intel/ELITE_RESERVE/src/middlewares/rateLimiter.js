/* * PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
 * PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
 * MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
 * ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
 */

const rateLimit = require('express-rate-limit');

const apiLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // Ventana de 15 minutos
  max: 100, // Máximo 100 peticiones por IP
  message: {
    status: 429,
    message: "Aura Intel ha detectado demasiadas peticiones. Acceso restringido temporalmente."
  },
  standardHeaders: true, // Retorna info en los headers 'RateLimit-*'
  legacyHeaders: false,
});

// Limitador específico para Login (Más estricto)
const loginLimiter = rateLimit({
  windowMs: 60 * 60 * 1000, // 1 hora
  max: 5, // Solo 5 intentos fallidos permitidos por hora
  message: "Demasiados intentos de login. Tu IP ha sido mapeada como sospechosa."
});

module.exports = { apiLimiter, loginLimiter };
