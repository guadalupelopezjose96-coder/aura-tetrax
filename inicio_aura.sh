#!/bin/bash
echo "=================================================="
echo " INICIANDO PROTOCOLO AURA-TETRAX (ESTÁNDAR 1979) "
echo " ARQUITECTO: JEGL "
echo "=================================================="

# 1. Definir la ruta absoluta de la bóveda de binarios
BIN_PATH="/data/data/com.termux/files/usr/bin"

# 2. Verificación de Integridad Zero-Trust
cd $BIN_PATH || exit
sha256sum -c manifest.sha256 && echo "[100% OK] Manifiesto Validado: Integridad confirmada" || exit 1

# 3. Activación del Módulo de Identidad
$BIN_PATH/identidad --auth --verify

# 4. Auditoría Legal Pre-vuelo
$BIN_PATH/auditor_legal --run-check --compliance-strict

# 5. Purga Final de Residuos
$BIN_PATH/purga --full-system-balance

# 6. Lanzamiento del Núcleo Croma Sónica (Sin chrt para compatibilidad Android)
echo "[LOG] Invocando Aura-Tetrax Engine Pro..."
$BIN_PATH/aura-tetrax --mode bio-digital --frequency 432 --monitor-realtime
