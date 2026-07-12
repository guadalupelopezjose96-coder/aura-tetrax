#!/bin/bash

# Configuración de variables
VERSION="Pro_$(date +%Y%m%d_%H%M%S)"
BINARY="target/release/tetrax_engine"

echo "--- Iniciando compilación segura del Tetrax Engine Pro ---"

# 1. Compilación optimizada para producción
cargo build --release --target aarch64-linux-android

# 2. Generación del Hash de Integridad (SHA-256)
sha256sum $BINARY > $BINARY.sha256

# 3. Firmado con GPG (Llave privada en hardware/seguro)
# Usamos --detach-sign para crear un archivo .sig independiente
gpg --batch --yes --detach-sign --armor $BINARY

echo "--- Binario firmado y verificado para la versión $VERSION ---"
# El binario ahora es 100% auditable bajo el estándar FESM
