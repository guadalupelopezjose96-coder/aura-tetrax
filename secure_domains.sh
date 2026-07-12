#!/bin/bash

# Lista de tus dominios registrados
DOMAINS=("auraintelcore.com" "fourphonix.com" "prophonix.com" "standard1979.com")
CONFIG_PATH="/etc/nginx/sites-available"

echo "Iniciando optimización al 100% bajo Standard 1979..."

for DOMAIN in "${DOMAINS[@]}"; do
    if [ -f "$CONFIG_PATH/$DOMAIN" ]; then
        echo "Aplicando seguridad a: $DOMAIN"
        
        # Insertar cabeceras de seguridad antes del cierre del bloque server
        sed -i '/server_name/a \
        # Cabeceras de Seguridad Standard 1979 \
        add_header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload" always; \
        add_header X-Frame-Options "SAMEORIGIN" always; \
        add_header X-Content-Type-Options "nosniff" always; \
        add_header Referrer-Policy "no-referrer-when-downgrade" always; \
        add_header Content-Security-Policy "default-src '\''self'\'' http: https: data: blob: '\''unsafe-inline'\''" always;' "$CONFIG_PATH/$DOMAIN"

        echo "Configuración completada para $DOMAIN"
    else
        echo "Aviso: Archivo para $DOMAIN no encontrado en $CONFIG_PATH"
    fi
done

# Verificar sintaxis de Nginx
nginx -t && systemctl reload nginx
echo "Despliegue finalizado al 100%."
