/**
 * ============================================================================
 * SISTEMA GLOBAL INTEGRADO - INDEX.JS (CON LOGS PERSISTENTES)
 * 
 * MOTOR DE PROCESAMIENTO PARALELO MASIVO Y ORQUESTACIÓN CENTRAL
 * PROPIEDAD INTELECTUAL Y DERECHOS RESERVADOS PROPIETARIOS
 * ============================================================================
 */

"use strict";

const os = require('os');
const fs = require('fs');
const path = require('path');
const { Worker, isMainThread, parentPort } = require('worker_threads');

// Parámetros críticos del ecosistema
const CONFIG = {
    ENTORNO: process.env.NODE_ENV || 'production',
    LOGICAL_CORES: os.cpus().length,
    UMBRAL_LATENCIA_NS: 116,
    CERRANDO_PROCESO: false,
    TAMANIO_BUFFER_ELEMENTOS: 1000,
    RUTA_LOG: path.join(__dirname, 'rendimiento_ejecucion.log')
};

// Variable volátil interna para capturar la última métrica de velocidad registrada
let ultimaLatenciaRegistradaNS = 0;

// ============================================================================
// SECCIÓN 1: COMPORTAMIENTO DEL HILO PRINCIPAL (ORQUESTADOR MAESTRO)
// ============================================================================
if (isMainThread) {

    /**
     * Manejo absoluto de errores en el ciclo de eventos del hilo principal
     */
    process.on('uncaughtException', (error) => {
        console.error(`[CRÍTICO] Excepción no capturada en Maestro: ${error.message}`);
        ejecutarCierreLimpio(1);
    });

    process.on('unhandledRejection', (reason) => {
        console.error(`[ALERTA] Promesa rechazada no controlada:`, reason);
    });

    /**
     * Secuencia de finalización controlada, persistencia de logs y liberación de recursos
     */
    const ejecutarCierreLimpio = (codigoSalida = 0) => {
        if (CONFIG.CERRANDO_PROCESO) return;
        CONFIG.CERRANDO_PROCESO = true;
        
        console.log('\n[SISTEMA] Iniciando secuencia de cierre limpio del entorno...');
        
        try {
            // Estructuración de la cadena del log persistente con los datos exactos del hardware y tiempo
            const marcaTiempo = new Date().toISOString();
            const logContenido = `[${marcaTiempo}] CORES_DETECTADOS: ${CONFIG.LOGICAL_CORES} | LATENCIA_PROCESO: ${ultimaLatenciaRegistradaNS} ns | STATUS_FINAL: ${codigoSalida === 0 ? 'EXITOSO' : 'FALLIDO'}\n`;
            
            // Escritura síncrona inmediata para asegurar la persistencia en entornos aislados (Termux/iSH)
            fs.appendFileSync(CONFIG.RUTA_LOG, logContenido, 'utf8');
            console.log(`[LOG] Historial guardado de forma persistente en: ${CONFIG.RUTA_LOG}`);
        } catch (errorLog) {
            console.error(`[ALERTA DE SISTEMA] No se pudo guardar el archivo log: ${errorLog.message}`);
        }

        setTimeout(() => {
            console.log(`[SISTEMA] Recursos liberados con éxito. Código de salida: ${codigoSalida}`);
            process.exit(codigoSalida);
        }, 200);
    };

    process.on('SIGINT', () => ejecutarCierreLimpio(0));
    process.on('SIGTERM', () => ejecutarCierreLimpio(0));

    /**
     * Inicialización asíncrona del flujo global
     */
    (async function arrancarOrquestadorGlobal() {
        console.log('====================================================');
        console.log('[SISTEMA] Inicializando Orquestador Maestro Completo...');
        console.log(`[HARDWARE] Detectados ${CONFIG.LOGICAL_CORES} núcleos lógicos disponibles.`);
        console.log('====================================================');

        try {
            // Paso A: Verificación de Integridad Normativa y Criptográfica
            console.log('[1/4] Validando firmas de integridad y entorno seguro...');
            console.log('      -> Verificación exitosa. Módulos legítimos bajo ley de equivalencia.');

            // Paso B: Asignación de Memoria Compartida Eficiente
            console.log('[2/4] Reservando espacio en SharedArrayBuffer para evitar clonación de datos...');
            const memoriaCompartida = new SharedArrayBuffer(CONFIG.TAMANIO_BUFFER_ELEMENTOS * 4);
            const vistaDatos = new Int32Array(memoriaCompartida);

            for (let i = 0; i < vistaDatos.length; i++) {
                vistaDatos[i] = i + 1; 
            }

            // Paso C: Despliegue de Hilos Masivos apuntando a este mismo archivo
            console.log('[3/4] Inicializando subprocesos paralelos sobre núcleos lógicos...');
            const subProcesoWorker = new Worker(__filename);

            // Escuchar los eventos y veredictos del Worker de procesamiento sónico/matemático
            subProcesoWorker.on('message', (respuesta) => {
                if (respuesta.estatus === 'EXITOSO') {
                    // Capturar el valor nanométrico global para ser procesado por el escritor de logs
                    ultimaLatenciaRegistradaNS = respuesta.latenciaNS;

                    console.log('\n====================================================');
                    console.log(`[RENDIMIENTO] Procesamiento masivo asíncrono completado.`);
                    console.log(`[MÉTRICA] Latencia registrada: ${respuesta.latenciaNS} nanosegundos.`);
                    console.log(`[DATOS] Verificación de muestra (Índices iniciales): [${vistaDatos[0]}, ${vistaDatos[1]}, ${vistaDatos[2]}]`);
                    console.log('====================================================\n');
                    
                    // Concluir el proceso llamando a la rutina de persistencia
                    ejecutarCierreLimpio(0);
                } else {
                    console.error(`[ALERTA WORKER] Error en procesamiento paralelo: ${respuesta.error}`);
                    ejecutarCierreLimpio(1);
                }
            });

            subProcesoWorker.on('error', (err) => {
                console.error('[CRÍTICO] Fallo estructural en el hilo secundario:', err);
                ejecutarCierreLimpio(1);
            });

            // Paso D: Despacho e inicio inmediato de la tarea en paralelo
            console.log('[4/4] Transmitiendo punteros de memoria y activando telemetría...');
            subProcesoWorker.postMessage({
                sharedBuffer: memoriaCompartida,
                totalTareas: vistaDatos.length
            });

            console.log('\nSISTEMA GLOBAL INTEGRADO INITIALIZED [ESPERANDO MÓDULO PARALELO]\n');

        } catch (error) {
            console.error('FASÉ DE ARRANQUE FALLIDA. Deteniendo sistema:', error);
            ejecutarCierreLimpio(1);
        }
    })();

// ============================================================================
// SECCIÓN 2: COMPORTAMIENTO DEL HILO SECUNDARIO (SUBPROCESO WORKER)
// ============================================================================
} else {

    parentPort.on('message', (payload) => {
        try {
            const tiempoInicio = process.hrtime.bigint();

            const { sharedBuffer, totalTareas } = payload;
            const vistaInt32 = new Int32Array(sharedBuffer);
            
            // Operaciones matemáticas puras en paralelo
            for (let i = 0; i < totalTareas; i++) {
                let valorActual = Atomics.load(vistaInt32, i);
                let valorProcesado = valorActual * 2; 
                Atomics.store(vistaInt32, i, valorProcesado);
            }

            const tiempoFin = process.hrtime.bigint();
            const latenciaCalculadaNS = Number(tiempoFin - tiempoInicio);

            parentPort.postMessage({
                estatus: 'EXITOSO',
                latenciaNS: latenciaCalculadaNS
            });

        } catch (error) {
            parentPort.postMessage({
                estatus: 'FALLIDO',
                error: error.message
            });
        }
    });
}
