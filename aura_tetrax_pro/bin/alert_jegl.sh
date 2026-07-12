#!/bin/bash
LOG_FILE="/data/data/com.termux/files/home/watchdog.log"
# Palabras clave que indican una falla inminente
KEYWORDS=("panic" "error" "critical" "failed")

for word in "${KEYWORDS[@]}"; do
    if grep -q "$word" "$LOG_FILE"; then
        # Acción: Notificación en pantalla de Android (Requiere termux-api)
        termux-notification --title "¡ALERTA JEGL!" --content "Error detectado: $word. Revisar logs." --priority high
        
        # Opcional: Registro en log de alertas
        echo "[$(date)] [ALERTA] Se ha detectado una señal crítica: $word" >> /data/data/com.termux/files/home/alerts_jegl.log
        
        # Limpiamos las ocurrencias procesadas para no enviar notificaciones duplicadas
        sed -i "/$word/d" "$LOG_FILE"
    fi
done
