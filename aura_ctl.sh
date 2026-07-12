#!/bin/bash
# Orquestador Maestro Aura-Tetrax - Estándar 1979
# Autoridad: JEGL
while true; do
    echo "--- [AURA-TETRAX CONTROL PANEL: 100% OPERATIONAL] ---"
    echo "1. Inyectar Carga Fiscal (Hexakis)"
    echo "2. Verificar Centinela (Watchdog)"
    echo "3. Auditoría Sonora (Cromo Acústica)"
    echo "4. Radar Frecuencial (Tiempo Real)"
    echo "5. Protocolo de Sucesión (Cifrado)"
    echo "6. Salir"
    read -p "Seleccione protocolo (1-6): " opt
    case $opt in
        1) ~/hexakis_load.sh ;;
        2) ps aux | grep watchdog_aura.sh ;;
        3) ~/sonic_audit.sh ;;
        4) ~/radar_frecuencial.sh ;;
        5) ~/vault_sec.sh ;;
        6) exit 0 ;;
    esac
done
