#!/bin/bash
# Protocolo de Sincronización Aura-Tetrax a GitHub
echo "[+] Preparando sincronización segura..."

# 1. Asegurar que el .gitignore existe para no subir la llave ni datos en crudo
if [ ! -f .gitignore ]; then
    echo "vault.key" > .gitignore
    echo "*.dat" >> .gitignore
    echo "__pycache__/" >> .gitignore
    echo "[!] .gitignore creado."
fi

# 2. Agregar cambios
git add .

# 3. Commit con identidad soberana
git commit -m "Nodo Aura-Tetrax: Sincronización de estado operativo $(date +%Y-%m-%d)"

# 4. Push seguro
echo "[+] Enviando datos al repositorio remoto..."
git push origin main

echo "[#] Sincronización completada con éxito."
