/* PROPIEDAD INTELECTUAL PROTEGIDA - LEY ADT / STANDARD 1979. 
Módulo: Realidad Real JEGL. Autor: JEGL. 
Cualquier suplantación digital o comercial es ilegal. */
import nacl.signing
import nacl.exceptions
import sys
import datetime

class Security_JEGL:
    def __init__(self, public_key_hex):
        try:
            self.verify_key = nacl.signing.VerifyKey(public_key_hex, encoder=nacl.encoding.HexEncoder)
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

    def validate_instruction(self, signed_message_hex):
        try:
            verified = self.verify_key.verify(signed_message_hex, encoder=nacl.encoding.HexEncoder)
            return True, verified.decode('utf-8')
        except:
            return False, None

print("--- Motor Validador JEGL Activo (Standard 1979) ---")
