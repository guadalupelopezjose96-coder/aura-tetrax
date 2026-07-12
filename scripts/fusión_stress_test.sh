#!/bin/bash
# Prueba de Fusión de Redes - Verificación al 100%
echo "[TEST] Iniciando carga en 88 núcleos..."

# Generación de carga paralela distribuida
stress-ng --cpu 88 --io 4 --vm 2 --vm-bytes 128M --timeout 60s

echo "[TEST] Monitoreando estabilidad térmica..."
cat /sys/class/thermal/thermal_zone0/temp
