#!/bin/bash
# Centinela Aura-Tetrax (Watchdog)
# Autoridad: JEGL
FILE="$HOME/aura_tetrax/genesis_block_000.log"
HASH_FILE="$HOME/aura_tetrax/genesis.hash"

# 1. Establecer línea base si no existe
if [ ! -f "$HASH_FILE" ]; then
    sha256sum "$FILE" > "$HASH_FILE"
    echo "[100% INIT] Línea base de integridad establecida."
fi

# 2. Bucle de monitoreo
echo "[100% MONITORING] Centinela activo. Vigilando $FILE..."
while true; do
    CURRENT_HASH=$(sha256sum "$FILE" | awk '{print $1}')
    SAVED_HASH=$(cat "$HASH_FILE" | awk '{print $1}')

    if [ "$CURRENT_HASH" != "$SAVED_HASH" ]; then
        echo "[!!! ALERTA FORENSE !!!] DETECTADA INTRUSIÓN O ALTERACIÓN EN EL REGISTRO."
        echo "Cierre de sistema solicitado por seguridad."
        exit 1
    fi
    sleep 5
done
