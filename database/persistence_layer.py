# SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
# Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
# PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
# database/persistence_layer.py
import json

def guardar_transaccion_db(transaccion_data):
    """
    Persistencia inmutable: Cada transacción se guarda como un registro único.
    """
    with open("database/ledger.json", "a") as f:
        json.dump(transaccion_data, f)
        f.write("\n")
