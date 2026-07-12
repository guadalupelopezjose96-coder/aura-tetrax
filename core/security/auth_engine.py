from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def verificar_autenticidad(emisor, mensaje, firma):
    """
    Verifica que el mensaje fue firmado por la clave privada del emisor.
    Si la firma no coincide, el sistema rechaza la transacción al 100%.
    """
    try:
        emisor.clave_publica.verify(
            firma,
            mensaje,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception:
        return False
