# SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
# Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
# PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
from sdk_decryptor_pro_jegl import AuraDecryptor

# Instanciamos el decriptador
decryptor = AuraDecryptor()

# Datos secretos
secreto = "CONFIG_USUARIO:USR_001_ACCESO_TOTAL"
cifrado = decryptor.cifrar_paquete(secreto)

print(f"Dato Cifrado: {cifrado}")
print(f"Dato Descifrado: {decryptor.descifrar_paquete(cifrado)}")
