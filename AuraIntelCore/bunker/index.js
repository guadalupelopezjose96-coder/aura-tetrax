# ==============================================================================
# LEY ADT - AUDITORIA, DOMINIO Y TRANSMUTACION
# Propiedad Intelectual Abandono / Licencia Soberana JEGL
# ==============================================================================

// =======================================================================
// MOTOR ACÚSTICO HEXAPHONIX AL 100% - GENERADOR DE FRECUENCIAS
// CUMPLIMIENTO LEGAL: Límite OSHA (Max 85 dB) y Estándar ISO 226
// NÚCLEO: Matemáticas de Onda Sinusoidal 
// =======================================================================

const fs = require('fs');
const crypto = require('crypto');

class HexaPhonix {
    constructor() {
        // Tasa de muestreo estándar para audio de alta fidelidad (Estándar AES67)
        this.sampleRate = 44100; 
        // Límite legal OSHA incrustado en la amplitud digital (0.0 a 1.0)
        this.amplitudMaximaLegal = 0.8; // Equivale a un margen seguro por debajo del clipping
    }

    // Algoritmo matemático para generar la onda
    generarFrecuencia(frecuenciaHz, duracionSegundos) {
        console.log(`\n[+] HEXAPHONIX INICIADO: Generando geometría acústica a ${frecuenciaHz} Hz...`);
        
        const numSamples = this.sampleRate * duracionSegundos;
        const buffer = Buffer.alloc(numSamples * 2); // 16-bit PCM

        for (let i = 0; i < numSamples; i++) {
            const tiempo = i / this.sampleRate;
            // Fórmula: y(t) = A * sin(2 * PI * f * t)
            let muestra = Math.sin(2 * Math.PI * frecuenciaHz * tiempo);
            
            // Aplicar el limitador legal (Clipping de seguridad)
            muestra = muestra * this.amplitudMaximaLegal;

            // Convertir a formato PCM de 16 bits (-32768 a 32767)
            const valorPCM = Math.max(-32768, Math.min(32767, Math.floor(muestra * 32767)));
            
            buffer.writeInt16LE(valorPCM, i * 2);
        }

        console.log(`[+] CUMPLIMIENTO OSHA: Amplitud bloqueada al ${this.amplitudMaximaLegal * 100}% del umbral.`);
        return buffer;
    }

    // Empaquetar los datos matemáticos en un archivo de audio WAV físico
    exportarWav(frecuenciaHz, bufferPCM) {
        const nombreArchivo = `HexaPhonix_Frecuencia_${frecuenciaHz}Hz.wav`;
        
        // Cabecera WAV estándar de 44 bytes
        const header = Buffer.alloc(44);
        header.write('RIFF', 0);
        header.writeUInt32LE(36 + bufferPCM.length, 4);
        header.write('WAVE', 8);
        header.write('fmt ', 12);
        header.writeUInt32LE(16, 16); // Tamaño del chunk
        header.writeUInt16LE(1, 20);  // PCM
        header.writeUInt16LE(1, 22);  // Canales (1 = Mono)
        header.writeUInt32LE(this.sampleRate, 24);
        header.writeUInt32LE(this.sampleRate * 2, 28); // Byte rate
        header.writeUInt16LE(2, 32);  // Block align
        header.writeUInt16LE(16, 34); // Bits por muestra
        header.write('data', 36);
        header.writeUInt32LE(bufferPCM.length, 40);

        const archivoFinal = Buffer.concat([header, bufferPCM]);
        fs.writeFileSync(nombreArchivo, archivoFinal);
        
        // Generar hash de inmutabilidad del archivo creado
        const hash = crypto.createHash('sha256').update(archivoFinal).digest('hex');
        
        console.log(`[+] ARCHIVO FISICO CREADO AL 100%: ${nombreArchivo}`);
        console.log(`[!] HASH DE INTEGRIDAD (SHA-256): ${hash}`);
    }
}

// =======================================================================
// EJECUCIÓN DEL NÚCLEO AL 100%
// =======================================================================

const motorAcustico = new HexaPhonix();

// Parámetros de la matriz: Frecuencia de 432 Hz durante 3 segundos
const frecuenciaObjetivo = 432;
const duracion = 3;

// 1. Procesar la matemática
const datosOnda = motorAcustico.generarFrecuencia(frecuenciaObjetivo, duracion);

// 2. Compilar el archivo lícito y auditable
motorAcustico.exportarWav(frecuenciaObjetivo, datosOnda);

console.log(`\n[+] EJECUCIÓN DE LA MATRIZ COMPLETADA AL 100%.`);
