/* * PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
 * PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
 * MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
 * ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
 */

const nodemailer = require('nodemailer');
require('dotenv').config();

const sendDigitalProduct = async (customerEmail, licenseKey) => {
  console.log(`📧 Preparando el 100% del envío para: ${customerEmail}...`);

  // Sugerencia Extra 100%: Usar variables de entorno para tu correo de ventas
  const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
      user: process.env.SALES_EMAIL,
      pass: process.env.SALES_EMAIL_PASS // Recomendación: Usar App Password
    }
  });

  const mailOptions = {
    from: `"Aura Intel Sales" <${process.env.SALES_EMAIL}>`,
    to: customerEmail,
    subject: '✅ Entrega de Producto: Aura Intel Elite Core 100%',
    text: `¡Felicidades! Tu pago ha sido confirmado al 100%.\n\n` +
          `Tu código de licencia es: ${licenseKey}\n\n` +
          `Descarga tu instalador aquí: [TU_LINK_DE_DROPBOX_O_GITHUB_PRIVADO]\n\n` +
          `Gracias por elegir la seguridad Aura Intel.`,
    attachments: [
      {
        filename: 'setup.sh',
        path: './setup.sh' // Enviamos el instalador al 100%
      }
    ]
  };

  try {
    await transporter.sendMail(mailOptions);
    console.log("✅ PRODUCTO ENVIADO AL 100%. Venta completada.");
    return true;
  } catch (error) {
    console.error("❌ Fallo en el envío al 100%:", error);
    return false;
  }
};

module.exports = { sendDigitalProduct };
