# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

# COPYRIGHT: USPTO-JEGL-2026 - Propiedad Absoluta de la Federación Fourphonix
#!/bin/bash
echo "🔓 Desbloqueando Bóveda Aura Intel al 100%..."
openssl enc -aes-256-cbc -d -in .env.enc -out .env
if [ $? -eq 0 ]; then
    echo "✅ Acceso Concedido. Iniciando Servidor Elite..."
    node server.js
    echo "🔐 Cerrando Bóveda automáticamente..."
    rm .env
else
    echo "❌ Contraseña Incorrecta."
fi
