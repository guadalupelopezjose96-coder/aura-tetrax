#!/bin/bash
# Ruta automática al home de tu usuario
LOG_FILE="$HOME/nginx_integrity.log"
BACKUP_DIR="$HOME/nginx_golden_backups"
CONFIG_PATH="$HOME/sites-available"

echo "[$(date)] --- INICIANDO AUDITORÍA DE JUSTICIA ---" >> "$LOG_FILE"

for DOMAIN in "auraintelcore.com" "fourphonix.com" "prophonix.com" "standard1979.com"; do
    if diff "$CONFIG_PATH/$DOMAIN" "$BACKUP_DIR/$DOMAIN" > /dev/null; then
        echo "$DOMAIN: OK" >> "$LOG_FILE"
    else
        # Si hay cambio, registra la desviación para que Kivy se ponga en rojo
        echo "$DOMAIN: DESVIACIÓN DETECTADA" >> "$LOG_FILE"
        # Restaurar automáticamente para mantener la Justicia
        cp "$BACKUP_DIR/$DOMAIN" "$CONFIG_PATH/$DOMAIN"
        echo "$DOMAIN: Restaurado al estado original al 100%" >> "$LOG_FILE"
    fi
done
