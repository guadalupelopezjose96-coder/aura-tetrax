# SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
# Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
# PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
import pkcs11

# Ruta común para SoftHSM en entornos Linux/Termux
# Si tienes un dispositivo físico (token USB), la ruta variará según el driver del fabricante.
LIBRARY_PATH = '/usr/lib/libsofthsm2.so' 

def detectar_hardware():
    print("--- Iniciando diagnóstico de hardware criptográfico ---")
    try:
        lib = pkcs11.lib(LIBRARY_PATH)
        tokens = list(lib.get_tokens())
        
        if not tokens:
            print("Resultado: No se detectaron tokens/HSM. Verifica la conexión física.")
        else:
            for token in tokens:
                print(f"Hardware detectado al 100%:")
                print(f"  - Label: {token.label}")
                print(f"  - Serial: {token.serial}")
                print(f"  - Modelo: {token.model}")
                print("Estado: Operativo para firma digital.")
                
    except Exception as e:
        print(f"Error crítico en la conexión: {e}")
        print("Sugerencia: Asegúrate de que la ruta de 'libsofthsm2.so' es correcta.")

if __name__ == "__main__":
    detectar_hardware()
