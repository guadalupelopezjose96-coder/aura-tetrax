#!/bin/bash
# Ruta de tus logs
LOG_FILE="/data/data/com.termux/files/home/watchdog.log"
ARCHIVE_DIR="/data/data/com.termux/files/home/logs_archive"

# Crear directorio de archivo si no existe
mkdir -p "$ARCHIVE_DIR"

# Si el log pesa más de 1MB, lo rotamos
if [ $(stat -c%s "$LOG_FILE") -gt 1048576 ]; then
    TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
    mv "$LOG_FILE" "$ARCHIVE_DIR/watchdog_$TIMESTAMP.log"
    touch "$LOG_FILE"
    echo "[$(date)] [SISTEMA] Log rotado exitosamente." >> "$LOG_FILE"
fi
