#!/bin/bash
# Monitor de alertas JEGL 100% Optimizado

THRESHOLD=90 # Umbral de carga del 90%
LOG_FILE="core_alerts.log"

while true; do
    # Obtener el uso promedio de los 76 núcleos
    CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}' | cut -d. -f1)

    if [ "$CPU_USAGE" -gt "$THRESHOLD" ]; then
        echo "[ALERTA CRÍTICA] - $(date) - Carga al $CPU_USAGE%" >> $LOG_FILE
        # Acción 100% debida: Reducir prioridad de procesos no críticos
        renice +10 -u $(whoami)
        # Notificación visual
        echo -e "\e[31m[!] ADVERTENCIA: Carga Crítica en los 76 Núcleos. Optimizando...\e[0m"
    fi
    sleep 5
done
