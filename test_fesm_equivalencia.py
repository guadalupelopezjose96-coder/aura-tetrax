ñ# test_fesm_equivalencia.py
from decimal import Decimal
from core.fesm_engine import ejecutar_transaccion_mercado
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# 1. Función para cargar claves desde archivos
def cargar_clave_privada(nombre):
    with open(f"{nombre}_private.pem", "rb") as key_file:
        return serialization.load_pem_private_key(key_file.read(), password=None)

# 2. Función de firma (El "sello" digital)
def firmar_transaccion(clave_privada, mensaje):
    return clave_privada.sign(
        mensaje,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )

class Entidad:
    def __init__(self, id_entidad, saldo, clave_privada=None, clave_publica=None):
        self.id = id_entidad
        self.saldo = Decimal(saldo)
        self.clave_privada = clave_privada
        self.clave_publica = clave_publica

def test_ley_equivalencia_fiscal_transaccion_basica():
    # Cargar claves de seguridad
    priv_emisor = cargar_clave_privada("emisor")
    
    # Configuración de Entidades
    emisor = Entidad("USR001", '1000.00', clave_privada=priv_emisor)
    receptor = Entidad("USR002", '500.00')
    tesoreria = Entidad("TES001", '0.00')
    
    monto = Decimal('250.00')
    costo = Decimal('2.00')
    
    # Preparar y firmar
    mensaje = f"{emisor.id}:{receptor.id}:{monto}".encode()
    firma = firmar_transaccion(emisor.clave_privada, mensaje)
    
    # Ejecución blindada
    resultado = ejecutar_transaccion_mercado(emisor, receptor, tesoreria, monto, costo, firma)
    
    # Aserciones Legales
    assert resultado.estado == "EXITO"
    assert emisor.saldo == Decimal('748.00')
    assert receptor.saldo == Decimal('750.00')
    print("Prueba de Equivalencia Fiscal y Seguridad Criptográfica pasada al 100%.")

if __name__ == "__main__":
    test_ley_equivalencia_fiscal_transaccion_basica()

