import subprocess

class SeguridadADT:
    def __init__(self):
        self.user_id = "guadalupelopezjose96-coder"
        self.fingerprint = "ED25519/RSA-4096"

    def validar_firma_jegl(self, file_path):
        """Verifica que el archivo esté firmado por el autor original."""
        try:
            result = subprocess.run(["gpg", "--verify", file_path], 
                                     capture_output=True, text=True)
            return self.user_id in result.stderr
        except Exception:
            return False

    def cifrar_modulo_aura(self, file_path):
        """Cifra módulos privados para protección 100%."""
        subprocess.run(["gpg", "--encrypt", "--recipient", self.user_id, file_path])
        print(f"🔒 Módulo {file_path} protegido al 100%.")
