import os
import subprocess
from datetime import datetime

def sync_log_to_github(log_file="adt_audit_log.jsonl"):
    """
    Sincroniza el Log de la Ley ADT con el repositorio remoto.
    Respaldo legal externo al 100%.
    """
    try:
        # 1. Preparar los comandos de Git
        commit_message = f"Respaldo ADT - Estándar 1979 - {datetime.now().strftime('%Y-%m-%d %H:%M')}"
        
        # 2. Ejecutar la secuencia de comandos en el sistema
        # Asegúrate de estar en la carpeta de tu repositorio
        subprocess.run(["git", "add", log_file], check=True)
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        
        print(f"Sincronización exitosa: {commit_message}")
        return True
    except Exception as e:
        print(f"Error en la sincronización: {e}")
        return False

# Ejemplo de integración: 
# Puedes llamar a esta función cada 10 entradas nuevas en el log.
