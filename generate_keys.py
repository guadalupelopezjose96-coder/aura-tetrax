# Crea este archivo: nano generate_keys.py
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def generar_par_claves(nombre):
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    # Guardar clave privada
    with open(f"{nombre}_private.pem", "wb") as f:
        f.write(private_key.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.PKCS8, encryption_algorithm=serialization.NoEncryption()))
    # Guardar clave pública
    public_key = private_key.public_key()
    with open(f"{nombre}_public.pem", "wb") as f:
        f.write(public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo))
    print(f"Claves generadas para {nombre}")

generar_par_claves("emisor")
generar_par_claves("receptor")
