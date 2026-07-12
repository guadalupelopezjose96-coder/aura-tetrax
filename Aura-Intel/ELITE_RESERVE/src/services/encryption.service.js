/* * PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
 * PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
 * MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
 * ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
 */

const crypto = require('crypto');

const ALGORITHM = 'aes-256-gcm'; // El estándar de la industria
const IV_LENGTH = 16; // Vector de inicialización

/**
 * Cifra un texto usando una llave maestra
 */
const encrypt = (text, masterKey) => {
  const iv = crypto.randomBytes(IV_LENGTH);
  const key = crypto.scryptSync(masterKey, 'salt', 32); // Derivamos llave segura
  const cipher = crypto.createCipheriv(ALGORITHM, key, iv);

  let encrypted = cipher.update(text, 'utf8', 'hex');
  encrypted += cipher.final('hex');
  const tag = cipher.getAuthTag().toString('hex');

  // Devolvemos todo el paquete (IV + Tag + Mensaje)
  return `${iv.toString('hex')}:${tag}:${encrypted}`;
};

/**
 * Descifra el paquete para recuperar el mensaje original
 */
const decrypt = (content, masterKey) => {
  const [ivHex, tagHex, encryptedHex] = content.split(':');
  const key = crypto.scryptSync(masterKey, 'salt', 32);
  const iv = Buffer.from(ivHex, 'hex');
  const tag = Buffer.from(tagHex, 'hex');
  const decipher = crypto.createDecipheriv(ALGORITHM, key, iv);
  
  decipher.setAuthTag(tag);
  let decrypted = decipher.update(encryptedHex, 'hex', 'utf8');
  decrypted += decipher.final('utf8');
  
  return decrypted;
};

module.exports = { encrypt, decrypt };
