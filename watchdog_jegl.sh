#!/bin/bash
# Ruta absoluta del binario encontrada por find
BINARIO="/data/data/com.termux/files/home/tetrax_engine/target/release/tetrax_engine"
NOMBRE_PROCESO="tetrax_engine"

# Verificamos si el proceso NO está corriendo
if ! pgrep -x "$NOMBRE_PROCESO" > /dev/null
then
    echo "[$(date)] $NOMBRE_PROCESO detectado caído. Reiniciando..." >> /data/data/com.termux/files/home/watchdog.log
    # Ejecutamos el binario
    "$BINARIO" &
fi
