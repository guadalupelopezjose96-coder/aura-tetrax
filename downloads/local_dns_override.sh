# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

#!/bin/bash
# © 2026 JEGL - PROTOCOLO DE CONTINUIDAD OPERATIVA
# PROPÓSITO: PUENTEAR CLOUDFLARE PARA DESARROLLO LOCAL AL 100%

DOMINIOS=("standard1979.com" "fourphonix.com" "auraintelcore.com")
IP_LOCAL="127.0.0.1"

echo "🛡️ ACTIVANDO RESOLUCIÓN SOBERANA..."

# Backup del archivo hosts original
cp /etc/hosts /etc/hosts.bak

for dominio in "${DOMINIOS[@]}"; do
    # Eliminar entradas previas del dominio para evitar duplicados
    sed -i "/$dominio/d" /etc/hosts
    # Insertar la nueva resolución local
    echo "$IP_LOCAL $dominio" >> /etc/hosts
    echo "✅ $dominio -> $IP_LOCAL"
done

echo "🚀 ENTORNO LISTO: Ya puedes acceder a tus proyectos sin depender de terceros."
