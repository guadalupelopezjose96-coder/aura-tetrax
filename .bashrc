# =========================================================================
# CONFIGURACIÓN SOBERANA .BASHRC - JEGL 100% PRIVADO & PREMIUM
# =========================================================================

# --- [ ALIAS Y ENTORNO GLOBAL ] ---
alias v-update='pkg update && pkg upgrade -y'
alias v-bunker='cd ~/Aura-Tetrax'
alias sync-justicia='cd ~/vault && git pull && git add . && git commit -m "Auto-sync" && git push'

export AUTHOR="JEGL"
export NUCLEOS=76
export JEGL_CORE_DIR="$HOME/JEGL_PROJECTS/Aura_Premium"

# --- [ PROTOCOLO DE INICIO - TETRAX ENGINE PRO ] ---
clear

# 1. Dashboard Visual Térmico
if [ -f ~/Aura-Tetrax/v_thermal_vision.py ]; then
    python ~/Aura-Tetrax/v_thermal_vision.py
fi

# 2. Activación Computacional de Alta Densidad
if [ -f ~/Aura-Tetrax/v_core_unlock_76.py ]; then
    python ~/Aura-Tetrax/v_core_unlock_76.py
fi

# 3. Sintonía Sónica Modular de Reparación (Frecuencia Armónica)
if [ -f ~/Aura-Tetrax/v_audio_repair.sh ]; then
    ~/Aura-Tetrax/v_audio_repair.sh > /dev/null 2>&1 &
fi

# Volcado de estado de seguridad envolviendo texto estático de forma nativa
echo "---- [ SOBERANÍA DIGITAL ACTIVA AL 100% ] ---"

# --- [ SISTEMA INTERACTIVO DE COMANDOS DE DESARROLLO ] ---
alias v-vision='clear && python ~/Aura-Tetrax/v_thermal_vision.py'
alias jegl_core='cd ~/JEGL_Sovereign_Dev'
alias gcommit='git commit -S -m'
alias blindar_termux='find ~/ -type f \
    -not -path "*/.*" \
    -not -name "*.asc" \
    -not -name "*.gpg_pass" \
    -not -name "aura_core.sh" \
    -not -name "*.gpg" \
    -exec gpg --batch --yes --passphrase-file ~/.gpg_pass --detach-sign -a {} \;'

# Automatizaciones críticas de resguardo y auditoría legal
alias jegl_sync='for f in *.py; do [[ "$f" != "blindaje_jegl.py" && "$f" != "config_jegl.py" ]] && cp "$f" ~/Aura-Tetrax/backup_scripts/; done'
alias justicia='mkdir -p ~/.config/aura/backups && cp ~/.config/aura/core_config.json ~/.config/aura/backups/ && history -c && clear'
alias auditoria='python3 ~/AuraIntelCore/bunker/v_sello_adt_total.py'
# --- [ CORE ALIASES - AURA INTEL CORE & INTERFAZ MAESTRA ] ---
# Comillas simples estrictas para prevenir expansión prematura de variables en la shell
alias aura='cd $JEGL_CORE_DIR && ./aura_panel.sh'
alias aura-stress='cd $JEGL_CORE_DIR && ./stress_test.sh'
alias run_sello='python3 ~/AuraIntelCore/bunker/hexaphonix_core/v_sello_adt_total.py'

# Alias para monitorear el clúster sin entrar a configurar nada

# Función atómica para purificación inmediata de la tabla de procesos paralelos
aura-clean() {
    echo "🧹 Purificando hilos en paralelo..."
    pkill -f law_core_engine || true
    pkill -f sonic_geometry_engine || true
    echo "✅ Tabla de subprocesos unificada y limpia."
}
alias ir_ubuntu='proot-distro login ubuntu --user root --chroot-dir /root/test_render'
export GPG_TTY=$(tty)

# --- JEGL Security Protocol: Auto-Audit ---
echo "[*] Verificando integridad del Ecosistema Aura..."
# Usar ruta absoluta para evitar errores de cd
if [ -f "$HOME/AuraIntelCore/bunker/audit_check.sh" ]; then
    bash "$HOME/AuraIntelCore/bunker/audit_check.sh"
else
    echo "[!] Error: No se encuentra el script de auditoría en $HOME/AuraIntelCore/bunker/"
fi

export GEMINI_API_KEY="AQ.Ab8RN6KUyMs12XgCMXtLGErrBSE0c4_y2kTt1Qpasv0-tYh0XA" 
#cd ~/AuraIntelCore/bunker && nohup ./target/release/bunker > log_ejecucion_$(date +%F).log 2>&1 &
crond
alias aura='/root/AuraIntelCore/AuraIntelCore/audit_check.sh'

# Alias de control total para Aura-Tetrax
alias aura_start='./prod_start_fesm.sh'
export PYTHONPATH=$PYTHONPATH:/data/data/com.termux/files/home/bunker

export PATH=$PATH:$HOME/.local/bin

# --- INICIO DE PROTOCOLO DE SOBERANÍA JEGL 100% ---
# Validación automática de la Ley ADT
if gpg --verify ~/ley_adt.adt.asc ~/ley_adt.adt 2>/dev/null; then
    echo "Ley ADT verificada. Ecosistema Soberano al 100%."
else
    echo "ERROR: Fallo en validación de Ley ADT. Acceso denegado al 100%."
   # exit 1
fi
# --- FIN DE PROTOCOLO DE SOBERANÍA JEGL 100% ---
# --- ALIAS DE JUSTICIA DIGITAL JEGL 100% ---
alias invocar_justicia='_invocar_justicia()'
_invocar_justicia() {
    if [ -z "$1" ]; then
        echo "Uso: invocar_justicia [archivo_a_auditar]"
        return 1
    fi
    echo "Aplicando Justicia Maximisisisisimamente Justa a: $1"
    gpg --detach-sign --armor "$1"
    echo "Auditoría registrada y firmada al 100%."
}

export PS1="MiFrase100% > "
export LANG=es_ES.UTF-8
export LANGUAGE=es_ES.UTF-8

alias limpiar='clear'
alias actualizar='pkg update && pkg upgrade'
alias misarchivos='ls -la'
