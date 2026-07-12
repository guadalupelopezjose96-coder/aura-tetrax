# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

# COPYRIGHT: USPTO-JEGL-2026 - Propiedad Absoluta de la Federación Fourphonix
#!/bin/bash

echo "--------------------------------------------------"
echo "🛡️  BIENVENIDO AL INSTALADOR AURA INTEL ELITE CORE"
echo "--------------------------------------------------"
echo "🔄 Iniciando configuración al 100%..."

# 1. Instalar dependencias del sistema
pkg update && pkg upgrade -y
pkg install nodejs -y

# 2. Instalar módulos de Node.js al 100%
echo "📦 Instalando librerías de seguridad y cripto..."
npm install express helmet express-rate-limit dotenv bip39 ethereumjs-wallet ethereumjs-util crypto zod

# 3. Crear estructura de carpetas si no existe
mkdir -p src/services src/middlewares src/contracts

# 4. Verificar archivo de secretos
if [ ! -f .env ]; then
    echo "⚠️  ADVERTENCIA: No se encontró el archivo .env"
    echo "📝 Creando plantilla .env para el cliente..."
    echo "LICENSE_KEY=SOLICITAR_AL_VENDEDOR" > .env
    echo "LICENSE_SECRET=aura_intel_master_96" >> .env
    echo "CLIENT_ID=guadalupelopezjose96_user" >> .env
    echo "ENCRYPTION_KEY=$(node -e 'console.log(require("crypto").randomBytes(32).toString("hex"))')" >> .env
fi

echo "--------------------------------------------------"
echo "✅ INSTALACIÓN COMPLETADA AL 100%"
echo "🚀 Para iniciar: node server.js"
echo "--------------------------------------------------"
