# --- PROTOCOLO DE SEGURIDAD Y VERIFICACIÓN ---

# 1. Verificar integridad de permisos de llaves (debe ser -rw-------)
ls -l ~/JEGL_Core/backup/keys/JEGL_Private_Key.asc

# 2. Validación maestra de archivos (SHA-256 vs Registro)
sha256sum -c REGISTRO_HASHES.txt

# 3. Protocolo de firma para nuevos archivos (EULA/LOG/FESM)
# Reemplazar [ARCHIVO] por el nombre del documento a firmar
gpg --armor --clearsign [ARCHIVO]

# 4. Generación de huella digital para nuevos activos
# Útil para añadir nuevos registros a REGISTRO_HASHES.txt
sha256sum [NUEVO_ARCHIVO] >> REGISTRO_HASHES.txt

# 5. Comando de auditoría rápida de integridad
# Verifica si algún documento ha sido alterado desde la última sesión
sha256sum -c REGISTRO_HASHES.txt | grep -v "OK"

# 6. Sincronización Segura (Git LFS)
# Asegura que tus cambios locales estén respaldados en tu repositorio oficial
git add .
git commit -m "Actualización de protocolo y registros - JEGL - Caso 71204722"
git push origin main
