#!/bin/bash
# * * Copyright (c) 2026 José Emanuel Guadalupe López (JEGL).
# Script de Firma de Verdad Digital e Integridad Estructural.

echo "📦 [PIPELINE] Compilando law_core_engine en modo optimizado Release..."
cargo build --release

if [ $? -eq 0 ]; then
    echo "✅ [PIPELINE] Compilación exitosa."
    
    # Ruta donde el binario de Rust genera el recibo
    JSON_FILE="dist/law_core_engine/audit_receipt.json"
    
    if [ -f "$JSON_FILE" ]; then
        echo "🔐 [PIPELINE] Firmando Manifiesto Inmutable con Llave 0F2BFD08AC1EF7C..."
        # Firma el manifiesto usando tu clave criptográfica oficial
        gpg --local-user 0F2BFD08AC1EF7C --detach-sign --armor --yes "$JSON_FILE"
        echo "🏆 [PIPELINE] Proceso de Verdad Digital completado al 100%."
    else
        # Si el JSON se genera en la raíz por el contexto de ejecución, lo firma ahí
        if [ -f "audit_receipt.json" ]; then
            echo "🔐 [PIPELINE] Firmando Manifiesto detectado en raíz..."
            gpg --local-user 0F2BFD08AC1EF7C --detach-sign --armor --yes audit_receipt.json
        else
            echo "⚠️ [AVISO] Ejecuta el binario primero para inicializar la telemetría del JSON."
        fi
    fi
else
    echo "🚨 [CRÍTICO] Fallo en la compilación del núcleo de Rust."
    exit 1
fi
