# SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
# Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
# PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

# ############################################################# #
# #            MÓDULO DE GEOLOCALIZACIÓN TÁCTICA JEGL         # #
# #            PROPIEDAD INTELECTUAL PRIVADA JEGL             # #
# ############################################################# #

import stripe
import requests

def obtener_mapa_ventas():
    # Recuperar los últimos pagos 100% legales
    pagos = stripe.PaymentIntent.list(limit=10)
    puntos_geograficos = []

    for pago in pagos.data:
        # Extraemos la IP o el país registrado en el pago
        pais = pago.get('shipping', {}).get('address', {}).get('country', 'Desconocido')
        if pais != 'Desconocido':
            puntos_geograficos.append(pais)

    return puntos_geograficos

# Este dato se envía directamente a la interfaz de auraintelcore.com
