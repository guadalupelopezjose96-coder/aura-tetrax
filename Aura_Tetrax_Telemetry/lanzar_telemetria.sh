#!/bin/bash

# Configuración de Entorno
export JEGL_SIGNING_KEY=9ef45529c914d3cf909e25ae4697dbac62679a2783b27b140bb135614bdad6be
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
LOG_DIR="telemetria_logs"

# Crear directorio si no existe
mkdir -p "$LOG_DIR"
ARCHIVO_SALIDA="$LOG_DIR/log_$TIMESTAMP.log"

# Ejecución del motor de telemetría y captura
./target/release/aura-tetrax-telemetria > "$ARCHIVO_SALIDA"

# Auditoría Automática: Generar hash SHA-256 para integridad
SHA=$(sha256sum "$ARCHIVO_SALIDA" | cut -d ' ' -f 1)

# Registrar en el Libro Mayor (Ledger)
echo "[$TIMESTAMP] Archivo: $ARCHIVO_SALIDA | Hash: $SHA" >> LOG_AUDITORIA.md

echo "Reporte generado y auditado con éxito: $ARCHIVO_SALIDA"
