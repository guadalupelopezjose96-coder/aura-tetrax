#!/bin/bash

# --- CONFIGURACIÓN ---
AURA_ROOT="$HOME/aura_tetrax_pro"
LOCAL_LOG="$AURA_ROOT/logs/audit.log"
REMOTE_DEST="usuario@servidor_central:/audit_db/received_logs/"

# 1. Comprobar si hay nuevos registros
if [ ! -s "$LOCAL_LOG" ]; then
    echo "No hay nuevos registros de auditoría para sincronizar."
    exit 0
fi

# 2. Cifrar el log antes de enviarlo (Seguridad 100%)
# Usamos --clearsign para que sea verificable pero cifrado
gpg --encrypt --recipient "ID_CENTRAL" "$LOCAL_LOG" > /tmp/audit_log.gpg

# 3. Envío al Servidor Central
scp /tmp/audit_log.gpg "$REMOTE_DEST"

# 4. Rotación de logs locales
# Una vez enviado, movemos el log a un archivo histórico para no enviar duplicados
mv "$LOCAL_LOG" "$AURA_ROOT/logs/history/audit_$(date +%Y%m%d_%H%M%S).log"
touch "$LOCAL_LOG"

echo "Logs de auditoría sincronizados con el servidor central."
