#!/bin/bash
# =================================================================
# SYNC CORE JEGL - PROTOCOLO DE TRANSMISIÓN SEGURA
# =================================================================

echo "--- [JEGL] Iniciando Sincronización al 100% ---"

# Solo añadir archivos blindados
git add *.aura
git add blindaje_jegl.py
git add aura_loader.py

# Commit con firma JEGL
git commit -m "Update Aura Intel Core Modules - Protocol Standard 1979"

# Push a tu repositorio privado
git push origin main

echo "--- [OK] Sincronización Exitosa al 100% ---"
