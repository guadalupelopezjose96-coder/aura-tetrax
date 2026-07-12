#!/bin/bash

# Directorio de logs y libro mayor
LOG_DIR="telemetria_logs"
ARCHIVO_AUDITORIA="LOG_AUDITORIA.md"

echo "=== VIGILANCIA DE INTEGRIDAD AURA-TETRAX INICIADA ==="

while true; do
    # Verifica si el archivo de auditoría existe
    if [ -f "$ARCHIVO_AUDITORIA" ]; then
        # Lee cada línea del libro mayor
        while read -r linea; do
            # Extrae la ruta del archivo y el hash registrado
            ARCHIVO=$(echo "$linea" | awk '{print $4}')
            HASH_REGISTRADO=$(echo "$linea" | awk '{print $7}')
            
            # Realiza la validación si el archivo aún existe
            if [ -f "$ARCHIVO" ]; then
                HASH_ACTUAL=$(sha256sum "$ARCHIVO" | cut -d ' ' -f 1)
                
                if [ "$HASH_ACTUAL" != "$HASH_REGISTRADO" ]; then
                    echo "[!] ALERTA CRÍTICA: Integridad comprometida en $ARCHIVO"
                fi
            fi
        done < "$ARCHIVO_AUDITORIA"
    fi
    
    # Pausa de seguridad antes del siguiente ciclo
    sleep 30
done
