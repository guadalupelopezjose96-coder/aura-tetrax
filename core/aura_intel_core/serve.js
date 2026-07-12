/* * PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
 * PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
 * MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
 * ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
 */

const express = require('express');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const { checkLicense100 } = require('./src/services/license.service');
const { createSecureVault } = require('./src/services/wallet.service');
const { encrypt } = require('./src/services/encryption.service');
require('dotenv').config();

// 1. Verificación de Cobro al 100% antes de iniciar
checkLicense100();

const app = express();
app.use(helmet()); // Blindaje de cabeceras
app.use(express.json());

// 2. Escudo Anti-DDoS al 100%
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100,
  message: "🛡️ Aura Intel: Bloqueado por seguridad al 100%."
});
app.use(limiter);

// 3. Endpoint de Creación de Wallet Cifrada
app.post('/api/v1/vault/create', async (req, res) => {
  const wallet = await createSecureVault();
  const encryptedMnemonic = encrypt(wallet.mnemonic, process.env.ENCRYPTION_KEY);
  
  res.json({
    status: "100% Secure",
    address: wallet.address,
    vault_data: encryptedMnemonic
  });
});

app.listen(3000, () => console.log("🚀 Aura Intel Core Activo al 100% en puerto 3000"));
