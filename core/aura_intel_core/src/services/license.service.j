const crypto = require('crypto');
require('dotenv').config();

const checkLicense100 = () => {
  const expectedHash = crypto.createHmac('sha256', process.env.LICENSE_SECRET)
                             .update(process.env.CLIENT_ID)
                             .digest('hex');

  if (process.env.LICENSE_KEY === expectedHash) {
    console.log("✅ LICENCIA VÁLIDA: Acceso al 100% concedido.");
  } else {
    console.error("❌ ERROR: Licencia Ilegal. El sistema se autodestruye.");
    process.exit(1); 
  }
};
module.exports = { checkLicense100 };
