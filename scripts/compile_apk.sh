# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

#!/bin/bash

# ============================================================
# AURA INTEL APK BUILDER v1.0
# 100% Automatización de Compilación | FourPhonix Core
# Generando el ejecutable para Android (ARM64-v8a)
# ============================================================

clear
echo "💠 INICIANDO PROCESO DE COMPILACIÓN AURA INTEL..."
sleep 1

# 1. Verificación de Recursos Críticos
echo "🔍 Comprobando Icono y Configuración..."
if [ -f "icon.png" ] && [ -f "buildozer.spec" ]; then
    echo "✅ Recursos detectados al 100%."
else
    echo "❌ ERROR: Falta icon.png o buildozer.spec en la raíz."
    exit 1
fi

# 2. Limpieza de Caché (Para evitar errores de versiones previas)
echo "🧹 Limpiando compilaciones antiguas..."
buildozer android clean

# 3. Compilación en Modo Debug (Para instalación directa en tu móvil)
echo "⚙️ Compilando APK con Tetrax Engine & Audio 3D..."
echo "⚠️ Este proceso puede tardar (depende de tu procesador)."
buildozer -v android debug

# 4. Resultado Final
if [ $? -eq 0 ]; then
    echo "🚀 [ÉXITO 100%] APK Generado en la carpeta /bin"
    ls -l bin/
else
    echo "❌ [FALLO] Revisa los logs de Buildozer."
fi
