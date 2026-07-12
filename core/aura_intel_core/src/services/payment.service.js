/* * PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
 * PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
 * MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
 * ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
 */

const { ethers } = require("ethers");
require('dotenv').config();

const verifyCryptoPayment = async (txHash, expectedAmount) => {
  console.log(`🔍 Monitoreando el 100% de la transacción: ${txHash}...`);
  
  // Recomendación 100%: Usar un proveedor de red (Sepolia para pruebas, Mainnet para cobrar real)
  const provider = new ethers.JsonRpcProvider(process.env.RPC_URL);
  
  try {
    const receipt = await provider.waitForTransaction(txHash);
    
    if (receipt && receipt.status === 1) {
      const tx = await provider.getTransaction(txHash);
      const amountReceived = ethers.formatEther(tx.value);

      if (amountReceived >= expectedAmount) {
        console.log(`✅ PAGO CONFIRMADO AL 100%: ${amountReceived} ETH recibidos.`);
        return true;
      }
    }
    console.log("❌ Pago insuficiente o fallido al 100%.");
    return false;
  } catch (error) {
    console.error("❌ Error en el mapeo de red al 100%:", error);
    return false;
  }
};

module.exports = { verifyCryptoPayment };
