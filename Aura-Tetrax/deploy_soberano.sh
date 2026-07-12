#!/bin/bash
# AURA-TETRAX: Despliegue Soberano
# Autor: JEGL

echo "[1/4] Compilando Núcleo Aura-Tetrax..."
cargo build --release --bin auditor_legal

if [ $? -eq 0 ]; then
    echo "[2/4] Ejecutando Auditoría Legal..."
    ./target/release/auditor_legal
    
    if [ $? -eq 0 ]; then
        echo "[3/4] Creando respaldo de integridad..."
        mkdir -p ./deploy/bin
        cp ./target/release/auditor_legal ./deploy/bin/
        
        echo "[4/4] Firmando despliegue de soberanía..."
        gpg --batch --yes --detach-sign --armor ./deploy/bin/auditor_legal
        
        echo "--------------------------------------------------------"
        echo "SISTEMA DESPLEGADO Y FIRMADO CON ÉXITO."
        echo "Ubicación: ./deploy/bin/auditor_legal"
        echo "Firma: ./deploy/bin/auditor_legal.asc"
        echo "--------------------------------------------------------"
    else
        echo "ERROR: La auditoría falló. Despliegue revocado."
        exit 1
    fi
else
    echo "ERROR: Fallo en compilación. Integridad comprometida."
    exit 1
fi
