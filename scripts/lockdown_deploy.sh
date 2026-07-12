#!/bin/bash
# Despliegue Global de Seguridad JEGL
NODOS=("usuario@samsung_local" "usuario@ipad_ip")

for nodo in "${NODOS[@]}"; do
    echo "[DEPLOY] Fortificando nodo: $nodo"
    # Copia del binario aura-core con el módulo de lockdown integrado
    scp ./aura-core "$nodo":/usr/local/bin/
    # Ejecución remota para asegurar permisos
    ssh "$nodo" "chmod 700 /usr/local/bin/aura-core"
    echo "[OK] Nodo $nodo blindado."
done
