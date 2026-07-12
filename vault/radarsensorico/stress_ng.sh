#!/bin/bash
# Script de Validación de Soberanía de Acceso - SOC v1.0

# 1. Definir variables de entorno (Asegúrate de tener GITHUB_TOKEN configurado)
REPO="guadalupelopezjose96-coder/stress-ng"
API_URL="https://api.github.com/repos/$REPO"

echo "Iniciando validación de soberanía para: $REPO"

# 2. Ejecutar consulta de validación
RESPONSE=$(curl -s -H "Authorization: token $GITHUB_TOKEN" -H "Accept: application/vnd.github.v3+json" $API_URL)

# 3. Analizar respuesta de la API
if [[ $RESPONSE == *"\"full_name\":\"$REPO\""* ]]; then
    echo "[SUCCESS] Acceso verificado al 100%. El repositorio es visible bajo tu firma."
else
    echo "[ERROR] Anomalía de acceso detectada. Verifica si el repositorio es privado o si el token ha expirado."
    echo "Respuesta de la API:"
    echo $RESPONSE
fi
