#!/bin/bash
# Protocolo de Rotación de Verdad Digital (JEGL-SOC)
# Ubicación: Aura-Tetrax-Elite-Core

LOGS=("fiscal_ledger" "synthesis.log" "persistence.log")
MAX_SIZE=5000 # KB

for log in "${LOGS[@]}"; do
    if [ -f "$log" ]; then
        size=$(du -k "$log" | cut -f1)
        if [ "$size" -gt "$MAX_SIZE" ]; then
            mv "$log" "$log.$(date +%Y%m%d_%H%M%S).bak"
            touch "$log"
            echo "[$(date +%T)] Rotación ejecutada: $log archivado." >> rotation.log
        fi
    fi
done
