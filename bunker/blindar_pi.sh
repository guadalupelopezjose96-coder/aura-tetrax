# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

#!/bin/bash
# Script de Blindaje de Propiedad Intelectual JEGL v100%

HEADER="// -----------------------------------------------------------------------
// PROPIEDAD INTELECTUAL - ESTATUS DE SOBERANÍA DIGITAL v
// AUTORÍA: JEGL (Justicia, Eficiencia, Gestión y Legalidad)
// PROYECTO: PROYECTO_ACTIVO - Protocolo El Cuadrado
//
// © 2026 JEGL. Todos los derechos reservados al 100%.
// -----------------------------------------------------------------------"

for file in $(find src -name "*.rs"); do
    if ! grep -q "AUTORÍA: JEGL" "$file"; then
        echo -e "$HEADER\n$(cat $file)" > "$file"
        echo "✅ Protegido: $file"
    else
        echo "🛡️ Ya cuenta con protección: $file"
    fi
done

