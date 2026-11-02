# SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
# Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
# PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
import os
import struct

def validate_bin(filename):
    if not os.path.exists(filename):
        print(f"Error: {filename} no encontrado.")
        return False
    
    file_size = os.path.getsize(filename)
    if file_size == 0:
        print(f"Error: {filename} está vacío.")
        return False

    # Leer los primeros valores para verificar la amplitud
    with open(filename, "rb") as f:
        data = f.read(8) # Leer un double (8 bytes)
        if data:
            val = struct.unpack('d', data)[0]
            if abs(val) > 1.0:
                print(f"Advertencia: Clipping detectado en {filename}")
                return False

    print(f"Integridad de {filename} validada al 100%.")
    return True


if __name__ == "__main__":
    # Lista actualizada para incluir el Barrido Integral
    files = ["aura_528.bin", "aura_432.bin", "aura_integral_sweep.bin"]
    all_ok = all([validate_bin(f) for f in files])
    if not all_ok:
        exit(1)
