# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

#!/bin/bash
# Matar procesos anteriores por si acaso
fuser -k 8080/tcp
# Activar Wakelock para que Android no duerma a Termux
termux-wake-lock
# Iniciar el servidor PHP en segundo plano
nohup php -S localhost:8080 > /dev/null 2>&1 &
echo "✅ Servidor PHP encendido en el puerto 8080"
# Iniciar el túnel de Cloudflare
echo "🚀 Iniciando Túnel de Cloudflare..."
cloudflared tunnel run --url http://localhost:8080 mitunel

