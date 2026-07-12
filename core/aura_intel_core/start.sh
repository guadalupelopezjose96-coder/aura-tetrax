# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

# COPYRIGHT: USPTO-JEGL-2026 - Propiedad Absoluta de la Federación Fourphonix
#!/bin/bash
echo "🔓 Desbloqueando Aura Intel Core 100%..."
openssl enc -aes-256-cbc -d -in .env.enc -out .env
if [ $? -eq 0 ]; then
    echo "✅ Acceso Concedido."
    node server.js
    rm .env
    echo "🔐 Bóveda Cerrada de forma debida."
else
    echo "❌ Error de Contraseña. El sistema permanece cifrado."
fi
