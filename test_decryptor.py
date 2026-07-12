from sdk_decryptor_pro_jegl import AuraDecryptor

# Instanciamos el decriptador
decryptor = AuraDecryptor()

# Datos secretos
secreto = "CONFIG_USUARIO:USR_001_ACCESO_TOTAL"
cifrado = decryptor.cifrar_paquete(secreto)

print(f"Dato Cifrado: {cifrado}")
print(f"Dato Descifrado: {decryptor.descifrar_paquete(cifrado)}")
