#!/bin/bash

# 1. Definir el timestamp
TIMESTAMP=$(date +%s)

# 2. Escribir el timestamp en un archivo temporal (evita errores de pipe)
echo -n "$TIMESTAMP" > timestamp.txt

# 3. Firmar el archivo creado
# Usamos -in para leer el archivo y -out para guardar la firma binaria
openssl pkeyutl -sign -inkey private.key -rawin -in timestamp.txt -out signature.bin

# 4. Convertir la firma binaria a Hexadecimal (asegurando 128 caracteres)
SIGNATURE=$(xxd -p -c 128 signature.bin | tr -d '\n')

# 5. Limpieza de archivos temporales
rm timestamp.txt signature.bin

# 6. Validar que la firma se generó correctamente
if [ ${#SIGNATURE} -lt 100 ]; then
    echo "ERROR: La firma generada es demasiado corta o inválida."
    exit 1
fi

echo "Timestamp: $TIMESTAMP"
echo "Firma: $SIGNATURE"
echo "Longitud: ${#SIGNATURE}"

# 7. Enviar la petición al Worker
curl -i \
  -H "X-Signature: $SIGNATURE" \
  -H "X-Timestamp: $TIMESTAMP" \
  -d "$TIMESTAMP" \
  https://mi-validador-edge.guadalupelopezjose96.workers.dev/
