from cryptography.fernet import Fernet

# Generar y guardar la llave (haz esto solo una vez)
def generar_llave():
    llave = Fernet.generate_key()
    with open("vault.key", "wb") as key_file:
        key_file.write(llave)

# Cifrar archivos de resultados
def cifrar_resultado(nombre_archivo):
    with open("vault.key", "rb") as key_file:
        llave = key_file.read()
    f = Fernet(llave)
    
    with open(nombre_archivo, "rb") as file:
        datos = file.read()
    
    datos_cifrados = f.encrypt(datos)
    
    with open(nombre_archivo + ".enc", "wb") as file:
        file.write(datos_cifrados)
    print(f"[!] Archivo {nombre_archivo} cifrado exitosamente.")

# generar_llave() # Descomentar solo la primera vez
# cifrar_resultado("resultados_fesm.txt")
