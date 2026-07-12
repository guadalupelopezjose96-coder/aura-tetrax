#!/bin/bash
LOG_FILE="/data/data/com.termux/files/home/watchdog.log"
CRITICAL_ERRORS=("panic" "segmentation fault" "critical" "error")

# 1. Monitoreo de existencia
if ! pgrep -x "tetrax_engine" > /dev/null; then
    echo "[$(date)] [ALERTA CRÍTICA] Proceso caído. Reiniciando..." >> "$LOG_FILE"
    /data/data/com.termux/files/home/tetrax_engine/target/release/tetrax_engine &
fi

# 2. Auditoría de contenido (Escaneo de errores)
for error in "${CRITICAL_ERRORS[@]}"; do
    if grep -iq "$error" "$LOG_FILE" | tail -n 20 | grep -q "$error"; then
        echo "[$(date)] [AUDITORÍA] Error crítico detectado: $error. Iniciando protocolo de recuperación." >> "$LOG_FILE"
        # Aquí podrías añadir una acción de limpieza, por ejemplo:
        # rm /data/data/com.termux/files/home/tetrax_engine/logs/temp_cache.tmp
    fi
done
