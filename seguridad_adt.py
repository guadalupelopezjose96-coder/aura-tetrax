/* PROPIEDAD INTELECTUAL PROTEGIDA - LEY ADT / STANDARD 1979. 
Módulo: Realidad Real JEGL. Autor: JEGL. 
Cualquier suplantación digital o comercial es ilegal. */
import nacl.signing
import nacl.exceptions

class Security_JEGL:
    def __init__(self, public_key_hex):
        # Cargamos tu llave pública ED25519 (Hexadecimal)
        self.verify_key = nacl.signing.VerifyKey(public_key_hex, encoder=nacl.encoding.HexEncoder)

    def validate_instruction(self, signed_message_hex):
        """
        Verifica que la instrucción provenga estrictamente de JEGL.
        """
        try:
            # Intentamos verificar el mensaje firmado
            verified = self.verify_key.verify(signed_message_hex, encoder=nacl.encoding.HexEncoder)
            return True, verified.decode('utf-8')
        except nacl.exceptions.BadSignatureError:
            return False, "ERROR: Firma inválida. Intento de acceso no autorizado detectado."

# --- Simulación de Operación ---
# Supongamos que esta es tu llave pública registrada en el sistema
# (Se extraería de tu configuración de GPG/SSH)
JEGL_PUBLIC_KEY = "..." 

security_system = Security_JEGL(JEGL_PUBLIC_KEY)

# Si una instrucción de "Actualización de Aura Intel" no viene firmada por ti, 
# el sistema bloquea el proceso al 100%.
