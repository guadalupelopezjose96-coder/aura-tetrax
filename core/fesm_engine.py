# core/fesm_engine.py
from decimal import Decimal, getcontext
import logging
from core.security.auth_engine import verificar_autenticidad

logging.basicConfig(filename='fesm_audit.log', level=logging.INFO, format='%(asctime)s - %(message)s')
getcontext().prec = 28

class TransaccionResultado:
    def __init__(self, estado, detalle):
        self.estado = estado
        self.detalle = detalle

def ejecutar_transaccion_mercado(emisor, receptor, tesoreria_red, monto, costo_red, firma):
    """
    Ejecuta la transacción SOLO si la firma digital es válida.
    """
    # 1. Preparar mensaje para verificación
    mensaje = f"{emisor.id}:{receptor.id}:{monto}".encode()

    # 2. Verificación de seguridad
    if not verificar_autenticidad(emisor, mensaje, firma):
        logging.warning(f"INTENTO DE FRAUDE: Firma inválida para Emisor {emisor.id}")
        return TransaccionResultado("ERROR", "Firma digital no válida")

    # 3. Lógica de transacción (Solo llega aquí si la firma es correcta)
    try:
        total_a_debitar = monto + costo_red
        if emisor.saldo < total_a_debitar:
            return TransaccionResultado("FALLIDO", "Fondos insuficientes")

        emisor.saldo -= total_a_debitar
        receptor.saldo += monto
        tesoreria_red.saldo += costo_red

        logging.info(f"OK | Emisor: {emisor.id} -> Receptor: {receptor.id} | Monto: {monto}")
        return TransaccionResultado("EXITO", "Transaccion auditada y verificada")

    except Exception as e:
        logging.error(f"FALLO | Error: {str(e)}")
        return TransaccionResultado("ERROR", str(e))
