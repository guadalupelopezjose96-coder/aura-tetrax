# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

#!/bin/bash
# 💠 HEARTBEAT DE FOURPHONIX - 100% DISPONIBILIDAD
while true; do
  if ! pgrep -f "capture_aura.py" > /dev/null; then
    echo "⚠️ [ALERTA] Caída de fase detectada. Resucitando el Aura..."
    python3 capture_aura.py &
  fi
  # Limpieza de logs basura para que nunca falte espacio en el A16
  find ./logs -name "*.tmp" -mtime +1 -delete
  sleep 5
done
