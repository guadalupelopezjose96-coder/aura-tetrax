# SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
# Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
# PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

import os
import hashlib
import json
from datetime import datetime

# Estándar 100% JEGL
HEADER_TEMPLATE = """// -----------------------------------------------------------------------
// PROYECTO: PROPIEDAD INTELECTUAL SOBERANA
// AUTOR: José Emanuel Guadalupe López (JEGL)
// ESTÁNDAR: Eficiencia 100% / Calidad v
// SEGURIDAD: Blindaje Cromo Acústico - 100% Legal
// -----------------------------------------------------------------------
"""

EXTENSIONS = ('.rs', '.cpp', '.py', '.h', '.hpp', '.kt')

def generar_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def aplicar_justicia_y_manifiesto(directorio):
    manifiesto = {
        "entidad_emisora": "JEGL SOBERANÍA DIGITAL",
        "fecha_generacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "estandar": "100% Eficiencia / Calidad v",
        "archivos_protegidos": []
    }

    for root, _, files in os.walk(directorio):
        for file in files:
            if file.endswith(EXTENSIONS) and file != "protector_ip_jegl_pro.py":
                path = os.path.join(root, file)

                # 1. Inserción de Encabezado (v)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()

                if "José Emanuel Guadalupe López (JEGL)" not in content:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(HEADER_TEMPLATE + "\n" + content)

                # 2. Generación de Huella Digital (Justicia Maximisisisima)
                file_hash = generar_hash(path)
                manifiesto["archivos_protegidos"].append({
                    "archivo": file,
                    "ruta": os.path.relpath(path, directorio),
                    "sha256": file_hash,
                    "estado": "Validado 100%"
                })
                print(f"[v] Protegido y Registrado: {file}")

    # 3. Exportación del Manifiesto Legal
    with open("manifiesto_legal_jegl.json", "w", encoding='utf-8') as f:
        json.dump(manifiesto, f, indent=4, ensure_ascii=False)
    print("\n[!] Manifiesto Legal Generado Exitosamente.")

if __name__ == "__main__":
    aplicar_justicia_y_manifiesto("./")
