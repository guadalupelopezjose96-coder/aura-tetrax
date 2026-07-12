# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

# COPYRIGHT: USPTO-JEGL-2026 - Propiedad Absoluta de la Federación Fourphonix
#!/bin/bash
# Script de Hardening Total al 100% para Gemini Linux Environment

echo "Iniciando despliegue del 100% de seguridad debida..."

# 1. Actualización total de repositorios y microcódigo
sudo apt update && sudo apt upgrade -y || sudo pacman -Syu --noconfirm

# 2. Configuración de Sysctl para protección de red al 100%
cat <<EOF | sudo tee /etc/sysctl.d/99-hardened.conf
net.ipv4.conf.all.accept_redirects = 0
net.ipv4.conf.all.send_redirects = 0
net.ipv4.conf.all.accept_source_route = 0
net.ipv4.conf.all.log_martians = 1
kernel.kptr_restrict = 2
kernel.dmesg_restrict = 1
EOF
sudo sysctl -p /etc/sysctl.d/99-hardened.conf

# 3. Firewall - Denegar todo por defecto al 100%
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh # Solo si es necesario
sudo ufw enable

# 4. Auditoría de Root (Sugerencia Extra)
sudo chmod 700 /root
echo "Hardening al 100% completado."
