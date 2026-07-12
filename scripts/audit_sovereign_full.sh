#!/bin/bash
# Auditoría Expandida: Licencia + Ley ADT
# Arquitecto Técnico JEGL | 2026-06-12

LICENSE_FILE="LICENSE_SOVEREIGN.md"
ADT_FILE="ADT_CONFIG.json"
MASTER_LICENSE="./MASTER_LICENSE_SOVEREIGN.md"
MASTER_ADT="./MASTER_ADT_CONFIG.json"

for repo_path in $(find . -maxdepth 2 -type d -name ".git"); do
    PROJECT_DIR=$(dirname "$repo_path")
    
    # 1. Verificar Licencia
    if [ ! -f "$PROJECT_DIR/$LICENSE_FILE" ]; then
        cp "$MASTER_LICENSE" "$PROJECT_DIR/$LICENSE_FILE"
        echo "[PROTECCIÓN] Licencia inyectada en $PROJECT_DIR"
    fi

    # 2. Verificar Configuración ADT
    if [ ! -f "$PROJECT_DIR/$ADT_FILE" ]; then
        cp "$MASTER_ADT" "$PROJECT_DIR/$ADT_FILE"
        echo "[PROTECCIÓN] Configuración ADT inyectada en $PROJECT_DIR"
    fi

    # 3. Commit de Verificación
    cd "$PROJECT_DIR"
    if [ -n "$(git status --porcelain)" ]; then
        git add .
        git commit -S -m "Auto-Aseguramiento: Licencia soberana y Ley ADT aplicadas al 100%"
        echo "[LOG] Repositorio $PROJECT_DIR consolidado al 100%"
    fi
    cd - > /dev/null
done

