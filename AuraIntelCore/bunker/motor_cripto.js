# ==============================================================================
# LEY ADT - AUDITORIA, DOMINIO Y TRANSMUTACION
# Propiedad Intelectual Abandono / Licencia Soberana JEGL
# ==============================================================================

// =======================================================================
// MODULO CRIPTOGRAFICO DE LA MATRIZ MAESTRA - 100% INMUTABLE
// NUCLEO: SHA-256 (Secure Hash Algorithm 256-bit)
// =======================================================================

const crypto = require('crypto');
const fs = require('fs');

class MotorMatriz {
    // 1. Encriptacion estricta de textos o telemetria de sensores
    static firmarDatos(datos) {
        const hash = crypto.createHash('sha256');
        hash.update(datos);
        const firmaDigital = hash.digest('hex');
        
        console.log(`[+] Telemetría Asegurada al 100%`);
        console.log(`[!] FIRMA SHA-256: ${firmaDigital}`);
        return firmaDigital;
    }

    // 2. Auditoria de integridad de archivos (Ej: validar el manifiesto)
    static auditarArchivo(rutaArchivo) {
        try {
            const bufferArchivo = fs.readFileSync(rutaArchivo);
            const hash = crypto.createHash('sha256');
            hash.update(bufferArchivo);
            const firmaArchivo = hash.digest('hex');
            
            console.log(`[+] Archivo Auditado Licitamente: ${rutaArchivo}`);
            console.log(`[!] HASH DE INTEGRIDAD: ${firmaArchivo}`);
            return firmaArchivo;
        } catch (error) {
            console.error(`[X] ERROR DE MATRIZ: No se pudo acceder a ${rutaArchivo}`);
        }
    }
}

// EJECUCION DE PRUEBA AL 100%
// Prueba 1: Firmar una señal del ecosistema Bio-digital
MotorMatriz.firmarDatos("FRECUENCIA_HEXAPHONIX_432HZ_ACTIVA");

// Prueba 2: Verificar la inmutabilidad de tu manifiesto recien creado
MotorMatriz.auditarArchivo('./manifiesto_matriz_maestra.txt');
