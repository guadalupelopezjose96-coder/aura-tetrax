/* * PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
 * PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
 * MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
 * ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
 */

const axios = require('axios');

async function attack() {
  console.log("⚔️ Iniciando bombardeo de peticiones...");
  for (let i = 1; i <= 10; i++) {
    try {
      const res = await axios.post('http://localhost:3000/api/login', {
        user: "admin", pass: "1234"
      });
      console.log(`Intento #${i}: ${res.data}`);
    } catch (err) {
      if (err.response && err.response.status === 429) {
        console.log(`Intento #${i}: 🛡️ BLOQUEADO POR AURA INTEL (429: Too Many Requests)`);
      } else {
        console.log(`Intento #${i}: ❌ Error de conexión.`);
      }
    }
  }
}
attack();
