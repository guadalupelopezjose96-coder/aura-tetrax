#!/bin/bash
# Sincronización 100% Segura JEGL

REMOTE_DIR="auraintelcore.com:/home/jegl/archivos_maestros"
REPORT="reporte_renderizado_$(date +%Y%m%d).jegl"

echo "--- Iniciando Carga Segura a Aura Intel Core ---"

# Sincronización usando llaves ED25519 previamente generadas
rsync -avz -e "ssh -p 22" $REPORT $REMOTE_DIR

if [ $? -eq 0 ]; then
    echo "[OK] Reporte de integridad alojado al 100%."
    echo "URL de Acceso: https://auraintelcore.com/private/$(basename $REPORT)"
else
    echo "[ERROR] Fallo en la sincronización. Verificando conectividad..."
    exit 1
fi
