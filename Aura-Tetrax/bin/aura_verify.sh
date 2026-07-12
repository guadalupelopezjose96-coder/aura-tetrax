#!/bin/bash
# Protocolo de Verificación Standard 1979
echo "[Thu Jun 25 20:51:21 EDT 2026] Iniciando Verificación de Integridad..."
cd ~/Aura-Tetrax
sha256sum -c checksums.sha256 --status
if [ $? -eq 0 ]; then
    echo "Integridad: 100% (Soberanía Confirmada)"
else
    echo "ERROR: Desviación detectada en la integridad del sistema."
    exit 1
fi
