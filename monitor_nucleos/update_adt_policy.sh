#!/bin/bash

# RUTA CORRECTA PARA TERMUX
AURA_ROOT="$HOME/aura_tetrax_pro"
CONFIG_FILE="$AURA_ROOT/config/adt_params.json"

# Asegurar que el directorio existe
mkdir -p "$AURA_ROOT/config"

# 1. PASO DE EDICIÓN
echo "Abriendo configuración para edición..."
nano "$CONFIG_FILE"

# 2. ACTUALIZACIÓN Y FIRMA (Se ejecuta tras cerrar nano)
NEW_VERSION="2026.05.23"
echo "Actualizando a versión $NEW_VERSION..."

# Es importante usar la ruta completa para gpg en el script
gpg --detach-sign --armor "$CONFIG_FILE"

# 3. Notificación
echo "Parámetros actualizados y firmados correctamente en $CONFIG_FILE.asc"
