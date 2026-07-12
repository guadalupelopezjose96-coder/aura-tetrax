# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

#!/bin/bash
# --- JEGL KEY ROTATION PROTOCOL ---

DATE=$(date +%Y%m%d)
BACKUP_DIR=~/.ssh/archive_$DATE

echo -e "\e[1;33m[INICIANDO ROTACIÓN DE LLAVES SOBERANAS]\e[0m"

# 1. Crear respaldo de llaves antiguas
mkdir -p $BACKUP_DIR
mv ~/.ssh/id_ed25519* $BACKUP_DIR/
echo "Respaldo creado en: $BACKUP_DIR"

# 2. Generar nueva llave ED25519
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519 -N "" -C "jegl-core-rotation-$DATE"

# 3. Mostrar nueva llave para actualización manual
echo -e "\n\e[1;32m[NUEVA LLAVE PÚBLICA GENERADA]\e[0m"
cat ~/.ssh/id_ed25519.pub

echo -e "\n\e[1;34m[PRÓXIMO PASO]\e[0m: Actualiza esta llave en GitHub para mantener tu acceso al 100%."
