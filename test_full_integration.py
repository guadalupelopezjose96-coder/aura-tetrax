# test_full_integration.py
from decimal import Decimal
from sdk_orchestrator_jegl import SDKOrchestrator
from core.fesm_engine import TransaccionResultado
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

# 1. Carga de claves (debe existir el archivo emisor_private.pem)
def cargar_clave_privada(nombre):
    with open(f"{nombre}_private.pem", "rb") as key_file:
        return serialization.load_pem_private_key(key_file.read(), password=None)

# 2. Firma real
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

# 3. Configuración del entorno
priv_emisor = cargar_clave_privada("emisor")
# Nota: Para la verificación, el objeto Emisor debe tener la clave pública cargada
# En un entorno real, cargarías la pública del archivo .pem correspondiente
emisor = Entidad("USR_001", "1000.00", clave_privada=priv_emisor)
emisor.clave_publica = priv_emisor.public_key() 

receptor = Entidad("USR_002", "500.00")
tesoreria = Entidad("TES_001", "0.00")
orquestador = SDKOrchestrator(tesoreria)

# 4. Construcción y Firma del Protocolo
monto = Decimal('100.00')
mensaje = f"{emisor.id}:{receptor.id}:{monto}".encode()
firma_real = firmar_transaccion(emisor.clave_privada, mensaje)

datos_transaccion = {
    'emisor': emisor,
    'receptor': receptor,
    'monto': monto,
    'costo': Decimal('1.00'),
    'firma': firma_real
}

# 5. Ejecución
print("Iniciando procesamiento a través del Orquestador...")
resultado = orquestador.procesar_comando("TRANSFERENCIA", datos_transaccion)

print(f"Estado Final del Sistema: {resultado.estado}")
print(f"Detalle: {resultado.detalle}")
