# database/persistence_layer.py
import json

def guardar_transaccion_db(transaccion_data):
    """
    Persistencia inmutable: Cada transacción se guarda como un registro único.
    """
    with open("database/ledger.json", "a") as f:
        json.dump(transaccion_data, f)
        f.write("\n")
