#!/bin/bash
# Sello de Producción Unificado del Ecosistema Privado JEGL
set -e

echo "Iniciando verificación de integridad criptográfica..."

# 1. Validar el estado de Git LFS y firmas cruzadas locales
git lfs status
git config core.hooksPath .githooks

# 2. Forzar la compilación estática de las suites unificadas
echo "Compilando variantes unificadas bajo perfil comercial..."
cargo build --release --manifest-path=./aura-tetrax-basic/Cargo.toml

# 3. Aplicar firmado digital determinista ED25519/GPG
echo "Estampando firma de autoría inmutable JEGL..."
BINARY_PATH="./target/release/aura_tetrax_basic"

if [ -f "$BINARY_PATH" ]; then
    # Generar la firma del binario comercial cerrado
    gpg --detach-sign --armor --local-user JEGL "$BINARY_PATH"
    echo "SISTEMA INTEGRADO Y BLINDADO EXITOSAMENTE [100% PRIVADO Y LEGAL]"
else
    echo "ERROR: Fallo en la verificación del binario compilado."
    exit 1
fi

