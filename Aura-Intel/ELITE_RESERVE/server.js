/* * PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
 * PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
 * MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
 * ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
 */

const express = require('express');
const helmet = require('helmet');
const { loginLimiter } = require('./src/middlewares/rateLimiter');

const app = express();
app.use(helmet()); // Capa de seguridad de headers
app.use(express.json());

// Esta es la ruta que vamos a proteger
app.post('/api/login', loginLimiter, (req, res) => {
  res.send("✅ Intento de login recibido (Procesando...)");
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`🛡️ Servidor Elite Core activo en http://localhost:${PORT}`);
  console.log(`⚠️ El limitador está activo: más de 5 intentos bloquearán la IP.`);
});
