#!/bin/bash

# 1. Datos a enviar
DATA='{"mensaje":"hola"}'
TIMESTAMP=$(date +%s)

# 2. Generar la firma usando tu private.key
# Esto crea una cadena hexadecimal única validable por tu Worker
SIGNATURE=$(echo -n "${DATA}${TIMESTAMP}" | openssl dgst -sha256 -sign private.key -hex | sed 's/.* //')

echo "Enviando datos con firma..."

# 3. Realizar la petición
curl -i \
  -H "X-Signature: $SIGNATURE" \
  -H "X-Timestamp: $TIMESTAMP" \
  -H "Content-Type: application/json" \
  -d "$DATA" \
  https://mi-validador-edge.guadalupelopezjose96.workers.dev/
