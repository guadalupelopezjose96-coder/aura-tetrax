/* PROPIEDAD INTELECTUAL PROTEGIDA - LEY ADT / STANDARD 1979. 
Módulo: Realidad Real JEGL. Autor: JEGL. 
Cualquier suplantación digital o comercial es ilegal. */
import hashlib
import json
import os
from datetime import datetime, timezone

class ImmutableADTLog:
    def __init__(self, log_file="adt_audit_log.json"):
        self.log_file = log_file
        # Inicializar el archivo si no existe
        if not os.path.exists(self.log_file):
            with open(self.log_file, "w") as f:
                json.dump([], f)

    def get_last_hash(self):
        """Recupera el último hash del historial para el encadenamiento."""
        try:
            with open(self.log_file, "r") as f:
                data = json.load(f)
                if not data:
                    return "0" * 64  # Hash génesis para la primera entrada
                return data[-1]["current_hash"]
        except (FileNotFoundError, json.JSONDecodeError):
            return "0" * 64

    def write_entry(self, txn_data):
        """Escribe una entrada inmutable encadenada bajo la Ley ADT."""
        prev_hash = self.get_last_hash()
        
        # Estructura de la entrada (Verdad Digital)
        entry_content = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "prev_hash": prev_hash,
            "data": txn_data,
            "law_standard": "Estándar 1979 - Equivalencia Fiscal"
        }
        
        # Generar el Hash SHA-256 (FIPS 180-4 Compliant)
        # Se usa sort_keys=True para garantizar que el hash sea siempre el mismo
        raw_payload = json.dumps(entry_content, sort_keys=True).encode()
        current_hash = hashlib.sha256(raw_payload).hexdigest()
        entry_content["current_hash"] = current_hash

        # Actualizar el archivo JSON
        try:
            with open(self.log_file, "r+") as f:
                logs = json.load(f)
                logs.append(entry_content)
                f.seek(0)
                json.dump(logs, f, indent=4)
                f.truncate()
            
            print(f"[JEGL-ADT] Entrada registrada con éxito. Hash: {current_hash[:16]}...")
            return current_hash
        except Exception as e:
            print(f"[ERROR-ADT] Fallo en la persistencia inmutable: {e}")
            return None

# --- EJECUCIÓN DE PRUEBA AL 100% ---
if __name__ == "__main__":
    logger = ImmutableADTLog()
    # Registro de prueba: Activación de Soberanía Digital
    logger.write_entry({
        "status": "Sincronización Exitosa",
        "repositorio": "guadalupelopezjose96-coder/Hexakis",
        "sistema": "Aura Intel Core - 76 Cores"
    })
