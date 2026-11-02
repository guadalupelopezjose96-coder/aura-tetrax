# SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
# Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
# PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
# config_data.py
from decimal import Decimal

# Diccionario de inicialización determinista para el estándar fiscal
CONFIGURACION_FISCAL_INMUTABLE = {
    "identificador_matriz": "FESM-1979-CORE",
    "version_framework": "PRO-ELITE-V1",
    "tasas_equivalencia": {
        "base_regulatoria": Decimal("1979.100000000000000000000000"),
        "factor_sustentabilidad": Decimal("1.000000000000000000000000"),
        "umbral_seguridad_maxima": Decimal("0.000000000000000000000001")
    },
    "frecuencias_sincronizacion": {
        "limpieza_armonica": Decimal("432.000000000000000000000000"),
        "transformacion_nucleo": Decimal("528.000000000000000000000000")
    }
}
