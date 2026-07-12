# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

#!/bin/bash
# Protocolo de Sincronización JEGL - Eficiencia 100%
# Uso: Sincroniza datos de transacciones eléctricas y código fuente

ORIGEN="$HOME/AuraIntelCore/data/"
DESTINO="192.168.1.72:/backup/FourPhonix-Core-JEGL-/"

echo "Iniciando Sincronización de Verdad Digital..."

# rsync con flags de integridad:
# -a: archivo (preserva permisos), -v: visual, -z: compresión, -e: cifrado SSH
rsync -avz -e ssh --progress $ORIGEN $DESTINO \
--exclude 'temp_*' \
--log-file="$HOME/logs/sync_adt.log"

echo "Sincronización al 100% Completada."
