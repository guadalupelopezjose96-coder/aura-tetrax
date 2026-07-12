#!/bin/bash
# Protocolo de Verdad Digital - Standard 1979
# Autor: José Emanuel Guadalupe López (JEGL)

echo "--- Iniciando Protocolo de Verdad Digital ADT ---"

# 1. Definir la Licencia de Identidad Real
LICENSE_TEXT="/* PROPIEDAD INTELECTUAL PROTEGIDA - LEY ADT / STANDARD 1979. 
Módulo: Realidad Real JEGL. Autor: JEGL. 
Cualquier suplantación digital o comercial es ilegal. */"

# 2. Inyectar licencia en archivos fuente (.cpp, .py, .rust)
for file in $(find . -maxdepth 2 -name "*.cpp" -o -name "*.py" -o -name "*.rs"); do
    if ! grep -q "LEY ADT" "$file"; then
        echo -e "$LICENSE_TEXT\n$(cat $file)" > "$file"
        echo "Protegiendo: $file"
    fi
done

# 3. Generar el Hash de Verdad Digital
echo "Generando Hash de Integridad..."
find . -type f -not -path '*/.*' | sort | xargs sha256sum > HASH_VERDAD_DIGITAL_JEGL.txt

echo "--- Blindaje 100% Completado bajo Standard 1979 ---"
