#!/bin/bash
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# PROTOCOLO DE CIERRE ELEGANTE PARA 88 NÚCLEOS

echo "⚠️ Iniciando secuencia de cierre ordenado del clúster..."

# 1. Terminar el watchdog para evitar re-resurrecciones
echo "Deteniendo Watchdog ADT..."
pkill -f watchdog.sh

# 2. Detener el núcleo principal y sus procesos asociados
echo "Finalizando procesos del filtro_soberano y escudo..."
pkill -f filtro_soberano.py
pkill -f v_transmitter_shield.py
pkill -f v_vigilante_jegl.sh

# 3. Limpieza final de sockets persistentes
echo "Limpiando sockets residuales..."
fuser -k 8888/tcp 2>/dev/null

echo "✅ Protocolo de Cierre JEGL finalizado. Clúster fuera de línea."
