# SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
# Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
# PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
import nacl.signing
import nacl.exceptions
import nacl.encoding

# 1. CONFIGURACIÓN (Simulamos tus llaves generadas)
# Generamos un par temporal para esta prueba, pero aquí irían tus llaves reales.
signing_key = nacl.signing.SigningKey.generate()
verify_key = signing_key.verify_key

pub_key_hex = verify_key.encode(encoder=nacl.encoding.HexEncoder).decode()
priv_key_hex = signing_key.encode(encoder=nacl.encoding.HexEncoder).decode()

print(f"--- INICIANDO PRUEBA DE INTEGRACIÓN LEY ADT ---")
print(f"Identidad JEGL cargada correctamente.\n")

# 2. FASE DE FIRMADO (Lo que haces tú)
mensaje_original = "ACCESO TOTAL AURA INTEL - EJECUCIÓN 76 NÚCLEOS"
signed_hex = signing_key.sign(mensaje_original.encode('utf-8'), encoder=nacl.encoding.HexEncoder).decode()

print(f"1. Instrucción firmada generada exitosamente.")

# 3. FASE DE VALIDACIÓN (Lo que hace el servidor/motor)
print(f"2. Verificando instrucción bajo Standard 1979...")

try:
    # El validador recibe la firma y usa la llave pública para verificar
    v_key = nacl.signing.VerifyKey(pub_key_hex, encoder=nacl.encoding.HexEncoder)
    v_key.verify(signed_hex, encoder=nacl.encoding.HexEncoder)
    
    print("\n[RESULTADO]: ✅ VALIDACIÓN 100% EXITOSA")
    print(f"AUTORIZADO: '{mensaje_original}'")
    print("Estado: Maximisisisima Justicia cumplida.")
    
except nacl.exceptions.BadSignatureError:
    print("\n[RESULTADO]: ❌ ERROR CRÍTICO")
    print("Estado: Intento de acceso no autorizado. Proceso bloqueado.")

