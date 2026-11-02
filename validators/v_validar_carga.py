# SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
# Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
# PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

import hashlib

def verificar_integridad(manifiesto_path):
    print("\033[0;36m[v] INICIANDO VALIDACIÓN DE TRANSBORDO JEGL...\033[0m")
    with open(manifiesto_path, 'r') as f:
        for linea in f:
            hash_esperado, nombre_archivo = linea.strip().split('  ')
            try:
                with open(nombre_archivo, 'rb') as af:
                    hash_real = hashlib.sha256(af.read()).hexdigest()
                
                if hash_real == hash_esperado:
                    print(f"[100% v] {nombre_archivo}: INTEGRIDAD VALIDADA")
                else:
                    print(f"[!] ERROR: {nombre_archivo} CORRUPTO O ALTERADO")
            except FileNotFoundError:
                print(f"[!] ERROR: {nombre_archivo} NO ENCONTRADO EN IPAD")

if __name__ == "__main__":
    verificar_integridad("manifiesto_JEGL.txt")
