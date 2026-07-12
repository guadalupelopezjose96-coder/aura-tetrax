#!/bin/bash
echo "--- INICIANDO RENDERIZADO MAESTRO JEGL (100% POTENCIA) ---"

# 1. Verificación de Identidad JEGL
echo "Verificando firmas ED25519..."
./secure_sign.sh --verify libfrequency_core.so
if [ $? -ne 0 ]; then
    echo "[!] ERROR: Firma no válida. Abortando por seguridad."
    exit 1
fi

# 2. Lanzamiento del Tetrax Engine Pro
# Optimizando para 76 núcleos y frecuencias de Sonic Geometry
nice -n -20 ./tetrax_engine --render --freq-base 432 --freq-alt 528 --threads 76 --output aura_output_01.wav

echo "--- RENDERIZADO COMPLETADO AL 100% ---"
