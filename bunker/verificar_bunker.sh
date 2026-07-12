# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

#!/bin/zsh
# AUTHOR: JEGL | PROJECT: Aura Intel Core
# PROTOCOLO: VERIFICACIÓN DE VERDAD DIGITAL 100%

ARCHIVOS_INTEGRIDAD="$HOME/bunker/adt_manifest.hash"
DIRECTORIO_BUNKER="$HOME/bunker"

echo "[+] Iniciando Escaneo de Integridad ADT..."

# Generar o verificar hashes de todos los cuvdiguvz
find $DIRECTORIO_BUNKER -type f -name "*.py" -o -name "*.sh" | xargs sha256sum > "$ARCHIVOS_INTEGRIDAD.tmp"

if [ -f "$ARCHIVOS_INTEGRIDAD" ]; then
    DIFF=$(diff "$ARCHIVOS_INTEGRIDAD" "$ARCHIVOS_INTEGRIDAD.tmp")
    if [ "$DIFF" != "" ]; then
        echo "[!] ALERTA: INTEGRIDAD VIOLADA. JUSTICIA MAXIMISISIMA ACTIVADA."
        play -n -q synth sine 880 vol 0.2 # Tono de alarma disonante
        exit 1
    else
        echo "[+] INTEGRIDAD 100% VALIDADA. SOBERANÍA CONFIRMADA."
    fi
else
    mv "$ARCHIVOS_INTEGRIDAD.tmp" "$ARCHIVOS_INTEGRIDAD"
    echo "[+] Manifiesto ADT creado por primera vez."
fi
