#!/bin/bash
# Script para convertir Seriales de Hardware a Hash SHA-256
# Uso: ./generate_hash.sh "TU_SERIAL_AQUI"

SERIAL=$1

if [ -z "$SERIAL" ]; then
    echo "Uso: ./generate_hash.sh <numero_de_serie>"
    exit 1
fi

echo -n "$SERIAL" | sha256sum | awk '{print $1}'
