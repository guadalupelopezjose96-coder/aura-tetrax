#!/bin/bash
# Motor Maestro Aura-Tetrax
LOG_FILE="$HOME/JEGL_PROJECTS/Aura_Premium/logs/sesiones.log"
AUDIO_DIR="$HOME/JEGL_PROJECTS/Aura_Premium/dist/sonic_geometry_engine"

case $1 in
  "432") FILE="aura_pure_432hz.wav" ;;
  "528") FILE="aura_pure_528hz.wav" ;;
  "combo") FILE="aura_pure_432_528_combinedhz.wav" ;;
  "stop") pkill mpv; echo "Motor detenido"; exit 0 ;;
  *) echo "Uso: ./start_session.sh {432|528|combo|stop}"; exit 1 ;;
esac

# Ejecución optimizada
nice -n 19 timeout 45m mpv --loop=inf "$AUDIO_DIR/$FILE" &
echo "[$(date)] Sesión iniciada: $FILE" >> "$LOG_FILE"
echo "Iniciando $FILE..."
