# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

# ========================================================
# GENERADOR DE MANIFIESTO DE CARGA - JEGL
# OBJETIVO: INTEGRIDAD TOTAL 100%
# ========================================================

echo "[v] Generando Manifiesto de Integridad..."
cd /sdcard/Download/

# Generar hashes SHA256 para tus archivos clave
sha256sum Aura_Tetrax_JEGL_Backup_v.tar.gz > manifiesto_JEGL.txt
sha256sum termux_backup_jegl.tar.gz >> manifiesto_JEGL.txt
sha256sum cromo_acustico_JEGL_100.pdf >> manifiesto_JEGL.txt

echo "[v] Manifiesto 'manifiesto_JEGL.txt' creado al 100%."
chmod 600 manifiesto_JEGL.txt
