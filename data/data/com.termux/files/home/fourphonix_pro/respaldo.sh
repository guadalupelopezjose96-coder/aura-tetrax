# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

#!/bin/bash
FECHA=$(date +%Y%m%d_%H%M)
ARCHIVO="Respaldo_Federacion_$FECHA.tar.gz"

echo "🔐 INICIANDO COMPRESIÓN DEL NODO CENTRAL..."
tar -czf ~/$ARCHIVO ~/fourphonix_pro

echo "✅ RESPALDO CREADO: $ARCHIVO"
echo "📍 UBICACIÓN: Carpeta principal (~/)"
echo "💡 Sugerencia: Mueve este archivo a tu Google Drive o envíalo por correo."
