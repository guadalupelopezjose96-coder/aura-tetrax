# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

#!/bin/bash

# ============================================================
# FOURPHONIX CLOUD INFRASTRUCTURE - SETUP v1.0
# [AURA INTEL NODO MAESTRO] - 100% AUTOMATIZADO
# ============================================================

clear
echo "💠 INICIANDO INSTALACIÓN DE AURA INTEL EN EL VPS..."
sleep 2

# 1. Actualización del Núcleo del Sistema
echo "⚙️ Optimizando Linux Ubuntu para Fase Áurea..."
sudo apt update && sudo apt upgrade -y

# 2. Instalación de Motores (Python, Pip, Flask)
echo "📦 Instalando Librerías de Ingeniería Sensorial..."
sudo apt install python3-pip python3-dev -y
pip3 install flask flask-cors numpy pillow

# 3. Apertura de Puertos Legales (Barter Port: 8080)
echo "🛡️ Configurando Firewall para el Nodo 8080..."
sudo ufw allow 8080/tcp
sudo ufw --force enable

# 4. Creación de la Estructura de Datos
mkdir -p aura_core/logs
cd aura_core

# 5. Mensaje de Éxito al 100%
echo "------------------------------------------------------------"
echo "🚀 [ÉXITO] INFRAESTRUCTURA FOURPHONIX ACTIVA"
echo "📡 IP DEL SERVIDOR: $(curl -s ifconfig.me)"
echo "🔗 PUERTO DE MANDO: 8080"
echo "------------------------------------------------------------"
echo "Copia tu main.py e index.html aquí y ejecuta: python3 main.py"
