#!/bin/bash
# Watchdog de máxima estabilidad
while true; do
    # 1. Verificación del núcleo
    if ! pgrep -f "start_jegl_core" > /dev/null; then
        ./bunker/start_jegl_core.sh --cores 88 > /dev/null 2>&1 &
    fi

    # 2. Integración de Rotación de Logs (Ahora DENTRO del bucle)
    if [ -f "fiscal_ledger" ] && [ $(du -k "fiscal_ledger" | cut -f1) -gt 5000 ]; then
        mv "fiscal_ledger" "fiscal_ledger.$(date +%Y%m%d_%H%M%S).bak"
        touch "fiscal_ledger"
        echo "[$(date +%T)] Rotación de Ledger completada." >> watchdog.log
    fi

    # 3. Pausa de 5 minutos
    sleep 300
done
