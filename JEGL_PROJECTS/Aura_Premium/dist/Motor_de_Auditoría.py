// Copyright (C) 2026 José Emanuel Guadalupe López (JEGL)
// 
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
// 
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
// GNU General Public License for more details.
// 
// You should have received a copy of the GNU General Public License
// along with this program. If not, see <https://www.gnu.org/licenses/>.

import json
import sys
import hashlib
from datetime import datetime

class LawAsCodeEngine:
    def __init__(self, manifest_path):
        self.manifest_path = manifest_path
        self.manifest = self._load_manifest()
        
    def _load_manifest(self):
        try:
            with open(self.manifest_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"[-] Error crítico al cargar el manifiesto legal: {e}")
            sys.exit(1)

    def verify_licensing(self):
        """Garantiza el cumplimiento del decreto de gratuidad irrevocable."""
        licensing = self.manifest.get("licensing", {})
        if not licensing.get("monetization_allowed") is False:
            return False, "VIOLACIÓN: Se detectó un intento de monetización en un módulo básico protegido."
        return True, "CONFORME: Cláusula de gratuidad irrevocable validada al 100%."

    def audit_transaction(self, total_inputs, total_outputs):
        """Ejecuta la auditoría determinista de equivalencia fiscal."""
        context = {
            "total_inputs": total_inputs,
            "total_outputs": total_outputs
        }
        
        rules = self.manifest.get("audit_rules", [])
        for rule in rules:
            if rule["rule_id"] == "RULE-001-FISCAL-EQUIVALENCE":
                # Evaluación determinista segura sin usar eval() inseguro
                success = context["total_inputs"] == context["total_outputs"]
                
                # Generar hash único del estado de auditoría para inmutabilidad
                state_string = f"{success}-{total_inputs}-{total_outputs}-{datetime.utcnow().isoformat()}"
                audit_hash = hashlib.sha256(state_string.encode('utf-8')).hexdigest()
                
                if success:
                    return {
                        "status": "APPROVED",
                        "rule_id": rule["rule_id"],
                        "hash": audit_hash,
                        "details": "Equivalencia fiscal verificada con éxito."
                    }
                else:
                    return {
                        "status": "REJECTED",
                        "rule_id": rule["rule_id"],
                        "hash": audit_hash,
                        "details": f"Asimetría fiscal detectada: Inputs ({total_inputs}) != Outputs ({total_outputs})"
                    }
                    
        return {"status": "ERROR", "details": "No se encontraron reglas aplicables."}

# ==========================================
# Ejemplo de Ejecución en Entorno de Prueba
# ==========================================
if __name__ == "__main__":
    # Simulación de la existencia del archivo de manifiesto en el entorno local
    dummy_manifest = {
        "manifest_version": "1.0.0",
        "project_id": "Aura-Core-Basic",
        "licensing": {"monetization_allowed": False},
        "audit_rules": [{"rule_id": "RULE-001-FISCAL-EQUIVALENCE"}]
    }
    
    with open("legal_manifest.json", "w") as f:
        json.dump(dummy_manifest, f)

    # Inicializar el motor de Law-as-Code
    engine = LawAsCodeEngine("legal_manifest.json")
    
    # 1. Validar Licencia Básica Gratis
    lic_status, lic_msg = engine.verify_licensing()
    print(f"[Licencia] {lic_msg}")
    
    # 2. Ejecutar Auditoría Fiscal con Balance de Equivalencia Correcto
    print("\n[Ejecutando Auditoría 1: Balance Equilibrado]")
    result_1 = engine.audit_transaction(total_inputs=5000, total_outputs=5000)
    print(json.dumps(result_1, indent=2, ensure_ascii=False))
    
    # 3. Ejecutar Auditoría Fiscal con Balance Asimétrico (Intento de fraude o error)
    print("\n[Ejecutando Auditoría 2: Balance Asimétrico]")
    result_2 = engine.audit_transaction(total_inputs=5000, total_outputs=4200)
    print(json.dumps(result_2, indent=2, ensure_ascii=False))
