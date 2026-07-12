# sdk_decryptor_pro_jegl.py
from cryptography.fernet import Fernet

class AuraDecryptor:
    def __init__(self, key=None):
        # Si no hay clave, generamos una maestra
        self.key = key or Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def cifrar_paquete(self, datos_plano):
        """Cifra información sensible para almacenamiento o transmisión."""
        return self.cipher.encrypt(datos_plano.encode())

    def descifrar_paquete(self, token_cifrado):
        """Descifra información bloqueada por el sistema."""
        try:
            return self.cipher.decrypt(token_cifrado).decode()
        except Exception:
            return "ERROR: Clave inválida o paquete corrompido"
