# SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
# Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
# PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
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
