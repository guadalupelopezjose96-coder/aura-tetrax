#!/bin/bash
# Script de Cierre de Licenciamiento y Conversión a Propiedad Privada [JEGL]
# Ejecución compatible con entornos Termux e iSH Shell

EULA_HEADER="// PROPRIETARY AND CONFIDENTIAL\n// Copyright (C) 2026 JEGL. All Rights Reserved.\n// This software is proprietary commercial asset distributed privately.\n// Unauthorized copying, distribution, or alteration is strictly prohibited.\n// Verification of license required for execution."

find . -type f \( -name "*.rs" -o -name "*.cpp" -o -name "*.h" \) | while read -r file; do
    # Remover marcas de licencias previas (MIT/Apache/GPL) si existieran
    sed -i '/Copyright/,/permissions/d' "$file"
    # Inyectar el encabezado de propiedad cerrada e inmutable
    echo -e "$EULA_HEADER\n$(cat "$file")" > "$file"
done

echo "Transición de metadatos de código completada al 100% [CERRADO]."

