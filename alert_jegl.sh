#!/bin/bash
LOG_FILE="/data/data/com.termux/files/home/watchdog.log"
# Palabras clave críticas
KEYWORDS=("panic" "error" "critical" "failed")

for word in "${KEYWORDS[@]}"; do
    if grep -q "$word" "$LOG_FILE"; then
        # Notificación solo si termux-api está instalado
        if command -v termux-notification > /dev/null; then
            termux-notification --title "¡ALERTA JEGL!" --content "Error detectado: $word" --priority high
        fi
        echo "[$(date)] [ALERTA] Señal crítica encontrada: $word" >> /data/data/com.termux/files/home/alerts_jegl.log
        # Limpiamos el log para no saturar
        sed -i "/$word/d" "$LOG_FILE"
    fi
done
