#!/bin/bash
# Script de Activación Creativa - JEGL
# Uso: ./focus.sh [alpha|theta|gamma]

case $1 in
  "alpha")
    echo "Activando modo Creatividad (Alpha 10Hz)..."
    mpv --loop=inf ~/music/frecuencias/10Hz_Alpha.flac &
    ;;
  "theta")
    echo "Activando modo Flujo (Theta 6Hz)..."
    mpv --loop=inf ~/music/frecuencias/6Hz_Theta.flac &
    ;;
  "gamma")
    echo "Activando modo Enfoque Lógico (Gamma 40Hz)..."
    mpv --loop=inf ~/music/frecuencias/40Hz_Gamma.flac &
    ;;
  *)
    echo "Uso: ./focus.sh {alpha|theta|gamma}"
    ;;
esac
