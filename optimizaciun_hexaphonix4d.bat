@echo off
title Optimizador Hexaphonix 4D - 100%% Legal
echo Iniciando optimizacion total del sistema...

:: 1. Cambiar al plan de energia de Maximo Rendimiento
powercfg -setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c

:: 2. Prioridad de Tiempo Real para el proceso principal (Cambia 'HexaRender.exe' por tu ejecutable)
start /Realtime "" "C:\Ruta\A\Tu\Software\HexaRender.exe"

:: 3. Prioridad Alta para la sub-utilidad 4D/Haptics
start /High "" "C:\Ruta\A\Tu\Software\HapticsControl.exe"

:: 4. Detener servicios que causan jitter y latencia (Opcional pero recomendado)
net stop SysMain /y
net stop TabletInputService /y

echo El 100%% de las sub-utilidades estan ahora en prioridad critica.
pause
