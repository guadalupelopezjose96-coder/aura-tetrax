#!/data/data/com.termux/files/usr/bin/bash
# ==============================================================================
# AMNESIA TÁCTICA MAESTRA - BÓVEDA KNOX
# Arquitecto: JEGL | Pine Hills, Florida
# Dominio: Purga Atómica y Esterilización Total
# ==============================================================================

exec 2>/dev/null

echo -e "\033[1;36m[AMNESIA MAESTRA] Ejecutando purga y esterilización al 100%...\033[0m"

# 1. Purga Atómica de Directorios Volátiles
rm -rf $PREFIX/tmp/* ~/.cache/* 2>/dev/null

# 2. Destrucción de Archivos de Historial Residual
history -c 2>/dev/null
rm -f ~/.zsh_history ~/.bash_history 2>/dev/null

# 3. Registro de Confirmación en el Repositorio Aura-Tetrax-
DIR_REPO="$HOME/Aura-Tetrax-"
if [ -d "$DIR_REPO" ]; then
    cd "$DIR_REPO" || exit 1

    cat << 'EOF' >> README.md

