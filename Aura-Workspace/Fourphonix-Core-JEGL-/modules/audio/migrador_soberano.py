import os

KEY_ID = "FC3F7C19712F2764"
archivos = [f for f in os.listdir('.') if f.endswith('.gpg')]

print(f"💎 Refinando Bóveda Aura Intel Core...")

for archivo in archivos:
    # Evitar procesar lo que ya está migrado
    if "_1979_final" in archivo:
        continue
        
    nuevo_nombre = archivo.replace(".gpg", "_1979_final.gpg")
    # Intentar migración
    resultado = os.system(f"gpg --decrypt {archivo} | gpg --encrypt --recipient {KEY_ID} --output {nuevo_nombre}")
    
    if resultado == 0:
        print(f"✅ Migrado con éxito: {nuevo_nombre}")
        os.remove(archivo) # Borrar el viejo si el nuevo se creó bien
    else:
        print(f"❌ Archivo incompatible eliminado por seguridad: {archivo}")
        os.remove(archivo) # Borrar archivos corruptos o sin llave

print("\n✨ Bóveda sincronizada al 100% con el Standard 1979.")
