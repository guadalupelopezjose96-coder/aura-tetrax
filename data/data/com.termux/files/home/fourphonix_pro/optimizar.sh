# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

#!/bin/bash
echo "🧹 INICIANDO OPTIMIZACIÓN DEL BÚNKER..."

# Cuenta cuántos respaldos hay
TOTAL=$(ls -1 ~/Respaldo_Federacion_*.tar.gz 2>/dev/null | wc -l)

if [ "$TOTAL" -gt 1 ]; then
    echo "🔍 Se encontraron $TOTAL respaldos. Manteniendo solo el más reciente..."
    # Lista los archivos por fecha y borra todos menos el más nuevo
    ls -t ~/Respaldo_Federacion_*.tar.gz | tail -n +2 | xargs rm -f
    echo "✨ Limpieza completada. Espacio optimizado."
else
    echo "🛡️ El búnker ya está optimizado (Solo hay 1 respaldo o ninguno)."
fi
