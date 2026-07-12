/**
 * ============================================================================
 * ARCHIVO DE PROCESAMIENTO PARALELO - WORKER.JS
 * 
 * MOTOR DE PROCESAMIENTO MASIVO ASÍNCRONO
 * PROPIEDAD INTELECTUAL Y DERECHOS RESERVADOS PROPIETARIOS
 * ============================================================================
 */

"use strict";

const { isMainThread, parentPort, workerData } = require('worker_threads');

// Validar que este archivo NUNCA se ejecute directamente en el hilo principal
if (isMainThread) {
    console.error("[ERROR] worker.js no puede ser ejecutado directamente. Debe ser invocado desde index.js.");
    process.exit(1);
}

/**
 * 1. ESCUCHA DE CANAL DE COMUNICACIÓN ABIERTO
 * Este bloque intercepta los mensajes o buffers enviados desde index.js
 */
parentPort.on('message', (payload) => {
    try {
        // Medición de rendimiento de entrada (Métrica de precisión)
        const tiempoInicio = process.hrtime.bigint();

        let resultado;

        // Verificar si la comunicación se realiza mediante Memoria Compartida Eficiente
        if (payload.sharedBuffer instanceof SharedArrayBuffer) {
            resultado = procesarMemoriaCompartida(payload.sharedBuffer, payload.tareas);
        } else {
            // Caída segura (Fallback) si se envían datos serializados estándar
            resultado = procesarCargaEstandar(payload.datos);
        }

        // Medición de rendimiento de salida
        const tiempoFin = process.hrtime.bigint();
        const latenciaOperacionNS = Number(tiempoFin - tiempoInicio);

        // Devolver el resultado optimizado al hilo principal junto con su métrica exacta
        parentPort.postMessage({
            estatus: 'EXITOSO',
            latenciaNS: latenciaOperacionNS,
            datos: resultado
        });

    } catch (error) {
        // Comunicación segura de fallos internos hacia el orquestador index.js
        parentPort.postMessage({
            estatus: 'FALLIDO',
            error: error.message
        });
    }
});

/**
 * 2. PROCESAMIENTO ULTRA-RÁPIDO (SharedArrayBuffer)
 * Lee y escribe directamente en la memoria compartida con operaciones atómicas.
 * Ideal para operaciones matemáticas puras o sincronización de frecuencias.
 */
function procesarMemoriaCompartida(sharedBuffer, totalTareas) {
    // Mapear el buffer compartido a una vista de enteros de 32 bits
    const vistaInt32 = new Int32Array(sharedBuffer);
    
    // Ejemplo de procesamiento matemático en paralelo sobre el arreglo compartido
    for (let i = 0; i < totalTareas; i++) {
        // Atomics asegura que ningún otro hilo altere el índice exacto en el mismo nanosegundo
        let valorActual = Atomics.load(vistaInt32, i);
        
        // [Aquí insertas la lógica matemática pura o transformaciones de geometría sónica]
        let valorProcesado = valorActual * 2; 
        
        Atomics.store(vistaInt32, i, valorProcesado);
    }

    return { bytesProcesados: vistaInt32.byteLength };
}

/**
 * 3. PROCESAMIENTO ESTÁNDAR (Fallback)
 * Manejo de cargas de trabajo que no requieren buffers de memoria directa.
 */
function procesarCargaEstandar(datos) {
    // Lógica convencional estructurada y segura
    if (!datos) return null;
    
    // Operación genérica de procesamiento de datos
    return Object.freeze({ ...datos, procesado: true, timestamp: Date.now() });
}
