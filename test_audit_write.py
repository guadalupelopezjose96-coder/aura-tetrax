from core.fesm_engine import ejecutar_transaccion_mercado
from decimal import Decimal

class Entidad:
    def __init__(self, saldo):
        self.saldo = Decimal(saldo)

emisor = Entidad(1000)
receptor = Entidad(500)
tesoreria = Entidad(0)

resultado = ejecutar_transaccion_mercado(emisor, receptor, tesoreria, Decimal(250), Decimal(2))
print(f"Resultado de la prueba: {resultado.estado}")
