#!/usr/bin/env bash
# ==============================================================================
# BUNDLE: CONFIGURACIÓN DE REPOSITORIOS HÍBRIDOS (AURA-TETRAX & PRO)
# AUTOR: José Emanuel Guadalupe López (JEGL)
# RUST 100% MASTERY - INFRAESTRUCTURA SEGURA
# ==============================================================================

set -e

echo "=== [1] Creando estructura de directorios de la fortaleza ==="
mkdir -p ~/Aura_Workspace/Aura-Tetrax-Public
mkdir -p ~/Aura_Workspace/Aura-Tetrax-Private

echo "=== [2] Generando Licencia Irrevocable GNU GPLv3 para el Núcleo Público ==="
cat << 'EOF' > ~/Aura_Workspace/Aura-Tetrax-Public/LICENSE
                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2026 José Emanuel Guadalupe López (JEGL)
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

100% LEY IRREVOCABLE: El 100% de todos los componentes base de Aura Core
contenidos en este repositorio son y permanecerán 100% gratis para todas
las poblaciones de manera perpetua bajo el amparo de esta licencia GPLv3.
Cualquier derivado debe mantener esta condición de apertura obligatoria.
EOF

echo "=== [3] Inicializando Repositorio Público (Open-Core) ==="
cd ~/Aura_Workspace/Aura-Tetrax-Public
git init
cat << 'EOF' > README.md
# Aura-Tetrax (Core Público Base)
Tecnología de automatización digital y bases lógicas de la Ley ADT.
- **Licencia:** GNU GPLv3 (100% Gratis de por vida).
- **Autoría:** José Emanuel Guadalupe López (JEGL).
EOF
git add LICENSE README.md

echo "=== [4] Inicializando Repositorio Privado (High-Performance) ==="
cd ~/Aura_Workspace/Aura-Tetrax-Private
git init
cat << 'EOF' > .gitignore
# Forzar el aislamiento absoluto de llaves y datos de producción
*.gpg
*.key
*.secret
config/production_env.json
EOF

cat << 'EOF' > README.md
# Tetrax Engine Pro (Módulos Privados)
- Optimización masiva para arquitecturas de 76 a 88 núcleos lógicos.
- Sincronización nativa de frecuencias a 432Hz y 528Hz.
- Manifiestos de producción y llaves criptográficas cripto-seguras.
EOF
git add .gitignore README.md

echo "=============================================================================="
echo " OK: Estructura creada con éxito en ~/Aura_Workspace"
echo " Recuerda firmar tus commits usando: git commit -S -m 'Mensaje'"
echo "=============================================================================="
