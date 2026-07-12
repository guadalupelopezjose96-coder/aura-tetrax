#!/bin/bash

# 1. Definir los datos a firmar
TIMESTAMP=$(date +%s)
DATA="{\"mensaje\":\"hola\"}" # Ejemplo de cuerpo de petición

# 2. Combinar los datos (esto debe coincidir con cómo los lee tu Worker)
MESSAGE="${DATA}${TIMESTAMP}"

# 3. Generar la firma (Usando SHA256 y tu clave privada)
# Asegúrate de tener tu archivo 'private.key' en esta carpeta
# Cambia la línea de SIGNATURE en tu script por esta:
SIGNATURE=$(echo -n "${DATA}${TIMESTAMP}" | openssl dgst -sha256 -sign private.key -binary | openssl base64 -A)

echo "Timestamp: $TIMESTAMP"
echo "Firma: $SIGNATURE"

# 4. Ejecutar el CURL con la firma real
curl -i \
  -H "X-Signature: $SIGNATURE" \
  -H "X-Timestamp: $TIMESTAMP" \
  -H "Content-Type: application/json" \
  -d "$DATA" \
  https://mi-validador-edge.guadalupelopezjose96.workers.dev/
