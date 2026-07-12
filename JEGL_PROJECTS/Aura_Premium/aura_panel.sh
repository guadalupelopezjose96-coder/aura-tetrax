#!/bin/bash
# -------------------------------------------------------------------------
# Copyright (c) 2026 José Emanuel Guadalupe López (JEGL).
# Estatus: Panel de Control CLI Maestro - Entorno Premium Unificado.
# -------------------------------------------------------------------------

# Importar terminal activa para firmas GPG fluidas si se requiere
export GPG_TTY=$(tty)

# Códigos de color ANSI para diseño de interfaz scannable
CLEAR="\033[0m"
BOLD="\033[1m"
CYAN="\033[36m"
GREEN="\033[32m"
PURPLE="\033[35m"
YELLOW="\033[33m"
RED="\033[31m"

show_header() {
    clear
    echo -e "${CYAN}${BOLD}=================================================================${CLEAR}"
    echo -e "${CYAN}${BOLD}          PANEL DE CONTROL MAESTRO - AURA INTEL CORE             ${CLEAR}"
    echo -e "${CYAN}${BOLD}       Ecosistema Inmutable Premium | Soberanía Tecnológica      ${CLEAR}"
    echo -e "${CYAN}${BOLD}=================================================================${CLEAR}"
    echo -e " Autor: ${BOLD}José Emanuel Guadalupe López (JEGL)${CLEAR}"
    echo -e " Arquitectura activa: ${GREEN}$(nproc) Hilos lógicos en paralelo${CLEAR}"
    echo -e " Llave criptográfica oficial: ${YELLOW}0F2BDFD08AC1EF7C${CLEAR}"
    echo -e "${CYAN}-----------------------------------------------------------------${CLEAR}"
}

while true; do
    show_header
    echo -e " ${BOLD}[1]${CLEAR} ${GREEN}Ejecutar Pipeline Maestro${CLEAR} (Compilar, Generar y Firmar Ley + Audio)"
    echo -e " ${BOLD}[2]${CLEAR} ${PURPLE}Lanzar Motor Sónico Aura-Tetrax${CLEAR} (Renderizar Trilogía .WAV)"
    echo -e " ${BOLD}[3]${CLEAR} ${YELLOW}Correr Suite de Estrés Masivo${CLEAR} (Validar estabilidad de hilos)"
    echo -e " ${BOLD}[4]${CLEAR} ${CYAN}Sincronizar Repositorio (Git Push)${CLEAR} (Firma Digital ED25519)"
    echo -e " ${BOLD}[5]${CLEAR} ${RED}Salir del Panel${CLEAR}"
    echo -e "${CYAN}-----------------------------------------------------------------${CLEAR}"
    echo -ne " ${BOLD}Selecciona una opción táctica de desarrollo:${CLEAR} "
    read -r opcion

    case $opcion in
        1)
            echo -e "\n${GREEN}🚀 Iniciando pipeline unificado...${CLEAR}"
            ./dist/law_core_engine/update_and_sign.sh
            echo -ne "\nPresiona Enter para volver al panel..."; read -r
            ;;
        2)
            echo -e "\n${PURPLE}📐 Ejecutando motor de síntesis de ondas...${CLEAR}"
            cd dist/sonic_geometry_engine && cargo run --release && cd ../..
            echo -ne "\nPresiona Enter para volver al panel..."; read -r
            ;;
        3)
            echo -e "\n${YELLOW}🔥 Inyectando ráfagas masivas de carga...${CLEAR}"
            ./stress_test.sh
            echo -ne "\nPresiona Enter para volver al panel..."; read -r
            ;;
        4)
            echo -e "\n${GREEN}📦 Sincronizando con GitHub de forma segura...${CLEAR}"
            cd ~/Aura-Tetrax
            git add .
            git commit -S -m "feat(sonic): integrar matriz expandida 432_528_combinedHz y manifiestos firmados" || true
            git push origin main --force
            echo -ne "\nPresiona Enter para volver al panel..."; read -r
            ;;
        5)
            echo -e "\n${RED}Cerrando sesión en el Panel de Control Maestro. Entorno protegido.${CLEAR}\n"
            exit 0
            ;;
        *)
            echo -e "\n${RED}⚠️ Opción no válida. Intenta de nuevo.${CLEAR}"
            sleep 1
            ;;
    esac
done
