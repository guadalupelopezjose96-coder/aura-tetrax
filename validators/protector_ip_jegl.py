# SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
# Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
# PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

import os

# Configuración del Estándar 100% JEGL
HEADER_TEMPLATE = """// -----------------------------------------------------------------------
// PROYECTO: PROPIEDAD INTELECTUAL SOBERANA
// AUTOR: José Emanuel Guadalupe López (JEGL)
// ESTÁNDAR: Eficiencia 100% / Calidad v
// SEGURIDAD: Blindaje Cromo Acústico - 100% Legal
// -----------------------------------------------------------------------
// ATENCIÓN: Este código es Propiedad Intelectual de JEGL.
// La Verdad Digital y la Justicia Maximisisisima rigen su ejecución.
// -----------------------------------------------------------------------
"""

EXTENSIONS = ('.rs', '.cpp', '.py', '.h', '.hpp')

def aplicar_justicia_intelectual(directorio):
    print(f"--- Iniciando validación de Propiedad Intelectual en: {directorio} ---")
    for root, _, files in os.walk(directorio):
        for file in files:
            if file.endswith(EXTENSIONS):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Evitar duplicidad para mantener eficiencia 100%
                if "José Emanuel Guadalupe López (JEGL)" not in content:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(HEADER_TEMPLATE + "\n" + content)
                    print(f"[v] Protegido: {file}")
                else:
                    print(f"[-] Ya validado: {file}")

if __name__ == "__main__":
    # Ajusta a la ruta de tu repositorio Fourphonix-Core-JEGL-
    ruta_proyecto = "./"
    aplicar_justicia_intelectual(ruta_proyecto)

