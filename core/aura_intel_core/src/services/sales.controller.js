/* * PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
 * PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
 * MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
 * ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
 */

const { verifyCryptoPayment } = require('./payment.service');
const { sendDigitalProduct } = require('./email.service');
const crypto = require('crypto');

const processFullSale100 = async (txHash, customerEmail, amount) => {
  // 1. Verificar el pago al 100%
  const isPaid = await verifyCryptoPayment(txHash, amount);

  if (isPaid) {
    // 2. Generar Licencia Única (Recomendación Extra)
    const licenseKey = crypto.createHmac('sha256', process.env.LICENSE_SECRET)
                             .update(customerEmail)
                             .digest('hex');

    // 3. Enviar el 100% de los archivos
    await sendDigitalProduct(customerEmail, licenseKey);
    
    console.log("💰 CICLO DE MONETIZACIÓN CERRADO AL 100% 💰");
  }
};
