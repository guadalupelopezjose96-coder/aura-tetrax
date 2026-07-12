# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

#!/bin/bash
while true
do
  # Verifica si el proceso del túnel está vivo
  if pgrep -x "cloudflared" > /dev/null
  then
    # Todo bien
    sleep 60
  else
    # ALERTA: El túnel se ha caído
    termux-vibrate -d 1000
    termux-notification --title "ALERTA FOURPHONIX" --content "El Búnker Final se ha desconectado. Reiniciando..."
    # Intenta reiniciar el túnel automáticamente
    nohup cloudflared tunnel --config ~/.cloudflared/config.yml run > bunker_log.txt 2>&1 &
    sleep 10
  fi
done
