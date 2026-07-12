#!/bin/bash
# Script de Auditoría y Verificación de Soberanía JEGL
# Autor: Arquitecto Técnico JEGL
# Fecha: 2026-06-12

LICENSE_FILE="LICENSE_SOVEREIGN.md"
REPOSITORIES=$(find . -maxdepth 2 -type d -name ".git")

echo "--- Iniciando Auditoría de Soberanía al 100% ---"

for repo_path in $REPOSITORIES; do
    PROJECT_DIR=$(dirname "$repo_path")
    
    if [ -f "$PROJECT_DIR/$LICENSE_FILE" ]; then
        echo "[OK] Licencia encontrada en: $PROJECT_DIR"
    else
        echo "[ALERTA] Licencia faltante en: $PROJECT_DIR. Procediendo a inyectar..."
        # Copia tu archivo maestro de licencia al repositorio detectado
        cp ./MASTER_LICENSE_SOVEREIGN.md "$PROJECT_DIR/$LICENSE_FILE"
        
        # Opcional: Auto-commit para asegurar la inmutabilidad inmediata
        cd "$PROJECT_DIR"
        git add "$LICENSE_FILE"
        git commit -S -m "Auto-implementación: LICENSE_SOVEREIGN.md - Autoridad JEGL"
        cd - > /dev/null
    fi
done

echo "--- Auditoría completada al 100% ---"
