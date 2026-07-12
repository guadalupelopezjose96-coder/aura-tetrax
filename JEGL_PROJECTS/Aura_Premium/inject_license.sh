#!/usr/bin/env bash
# ==============================================================================
# AUTOMATIZACIÓN DE CABECERAS LEGALES - 100% LEGAL & DEBIDO
# ARCHITECT: José Emanuel Guadalupe López (JEGL)
# ==============================================================================

set -e

# Texto de la cabecera estandarizada
LICENSE_HEADER=$(cat << 'EOF'
// Copyright (C) 2026 José Emanuel Guadalupe López (JEGL)
// 
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
// 
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
// GNU General Public License for more details.
// 
// You should have received a copy of the GNU General Public License
// along with this program. If not, see <https://www.gnu.org/licenses/>.
EOF
)

echo "=== Iniciando auditoría e inyección de cabeceras GPLv3 ==="

# Buscar archivos de Rust (.rs), C++ (.cpp, .h) y Python (.py)
find . -type f \( -name "*.rs" -o -name "*.cpp" -o -name "*.h" -o -name "*.py" \) | while read -r file; do
    
    # Evitar procesar el propio script o archivos en directorios ocultos de git
    if [[ "$file" == *"./.git"* || "$file" == *"inject_license.sh"* ]]; then
        continue
    fi

    # Verificar si el archivo ya contiene el aviso de copyright para no duplicarlo
    if ! grep -q "Copyright (C) 2026 José Emanuel Guadalupe López" "$file"; then
        echo "Inyectando cabecera legal en: $file"
        
        # Crear un archivo temporal con la licencia y el contenido original
        temp_file=$(mktemp)
        echo "$LICENSE_HEADER" > "$temp_file"
        echo "" >> "$temp_file" # Línea en blanco de separación
        cat "$file" >> "$temp_file"
        
        # Reemplazar el archivo original de forma segura
        mv "$temp_file" "$file"
    else
        echo "✓ Archivo ya protegido: $file"
    fi
done

echo "=== Proceso de blindaje completado al 100% ==="
