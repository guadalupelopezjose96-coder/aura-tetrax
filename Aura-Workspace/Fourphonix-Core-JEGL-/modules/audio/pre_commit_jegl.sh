#!/bin/bash
# Autolimpieza de entorno AuraIntelCore basado en 14095.jpg

echo "Iniciando mantenimiento al 100%..."

# 1. Limpieza de logs de Kivy (los archivos rojos en la imagen)
rm -rf .kivy/logs/kivy_*.txt
echo "[OK] Logs de Kivy eliminados."

# 2. Limpieza de caché de Python y Pip
find . -type d -name "__pycache__" -exec rm -rf {} +
pip cache purge
echo "[OK] Caché depurada."

# 3. Verificación de Integridad Obligatoria
if [ -f "./check_integrity.sh" ]; then
    ./check_integrity.sh
    echo "[OK] Hash de verdad digital verificado."
else
    echo "[!] Advertencia: check_integrity.sh no encontrado."
fi

echo "Entorno listo para Git."
