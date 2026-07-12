cat << 'EOF' > audit_push.sh
#!/bin/bash
# Auditoría JEGL - Soberanía Digital 100%

echo "[1/4] Limpiando residuos de compilación (target/)..."
# Eliminamos carpetas pesadas que bloquean GitHub
rm -rf tetrax_engine/target/
git rm -r --cached tetrax_engine/target/ 2>/dev/null

echo "[2/4] Aplicando Sellado de Verdad Digital (Ley ADT)..."
# Aseguramos que el script de blindaje se ejecute antes de subir
if [ -f "./adt_shield.sh" ]; then
    bash ./adt_shield.sh
else
    echo "Error: adt_shield.sh no encontrado."
fi

echo "[3/4] Indexando archivos ligeros..."
git add .gitignore *.py *.sh tetrax_engine/src/
# Forzamos que Git ignore archivos de más de 50MB que no sean LFS
find . -size +50M ! -path "./.git/*" -exec git rm --cached {} \;

echo "[4/4] Ejecutando Push a Bóveda GitHub..."
git commit -m "Sincronización JEGL: Aura Core Elite v1.0 - Limpio y Protegido"
git push origin main

echo "--- Proceso Finalizado al 100% ---"
EOF
