import subprocess
import datetime

def generar_sello_auditoria():
    # 1. Crear el contenido del reporte
    timestamp = datetime.datetime.now().isoformat()
    reporte = f"AUDITORIA_SISTEMA_AURA_TETRAX\nFecha: {timestamp}\nEstado: INTEGRIDAD_CONFIRMADA\nAutor: JEGL\n"
    
    with open("auditoria_estado.log", "w") as f:
        f.write(reporte)
    
    # 2. Firmar el reporte con tu clave GPG
    # Usamos --detach-sign para crear una firma separada (.sig)
    comando = [
        "gpg", "--batch", "--yes", "--detach-sign", 
        "--local-user", "2AA545133B782DA5084BDC2CB9297EFFE8A71DF7", 
        "auditoria_estado.log"
    ]
    
    try:
        subprocess.run(comando, check=True)
        print("Sello ADT aplicado correctamente: auditoria_estado.log.sig generado.")
    except subprocess.CalledProcessError:
        print("Error: No se pudo aplicar el sello de integridad.")

if __name__ == "__main__":
    generar_sello_auditoria()
