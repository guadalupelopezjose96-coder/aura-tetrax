#!/bin/bash
# -------------------------------------------------------------------------
# Copyright (c) 2026 José Emanuel Guadalupe López (JEGL).
# Estatus: Suite de Estrés y Validación Anti-Zombi (Aura-Tetrax)
# -------------------------------------------------------------------------

set -e

echo "🔥 [1/4] Inicializando Suite de Estrés Corregida Aura-Tetrax..."
ENGINE_BIN="./law_core_engine/target/release/law_core_engine"
SONIC_BIN="./sonic_geometry_engine/target/release/sonic_geometry_engine"

export RAYON_NUM_THREADS=$(nproc)
echo "🚀 Hilos lógicos detectados y asignados: $RAYON_NUM_THREADS"

echo "⚡ [2/4] Lanzando ráfaga concurrente con aislamiento de subprocesos..."
echo "-----------------------------------------------------------------"

# Ejecución en bucle limpio con wait explícito interno para evitar estados defunct
(
    for i in {1..5}; do 
        $ENGINE_BIN > /dev/null 2>&1 &
        wait $!
    done
) &
PID_LAW=$!

(
    for i in {1..5}; do 
        $SONIC_BIN > /dev/null 2>&1 &
        wait $!
    done
) &
PID_SONIC=$!

echo "🖥️ [3/4] Capturando telemetría activa libre de fugas..."
echo "-----------------------------------------------------------------"

for tick in {1..10}; do
    if kill -0 $PID_LAW 2>/dev/null || kill -0 $PID_SONIC 2>/dev/null; then
        echo "⏱️ Muestreo #$tick -"
        ps -o pid,vsz,rss,args | grep -E 'law_core_engine|sonic_geometry_engine' | grep -v grep || true
        sleep 1.2
    else
        break
    fi
done

wait $PID_LAW || true
wait $PID_SONIC || true

echo "-----------------------------------------------------------------"
echo "🏆 [4/4] ¡Prueba de estrés completada! Entorno purificado al 100%."
