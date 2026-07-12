import os
import sys
import subprocess

CRITICAL_PATHS = {
    "MOTOR_DINAMICO": "/data/data/com.termux/files/home/AuraIntelCore/core/motor_sonic.jar",
    "SANEADOR": "/data/data/com.termux/files/home/AuraIntelCore/aura_core_i",
    "CENTINELA": "/data/data/com.termux/files/home/AuraIntelCore/validadores/v_ley_adt_sentencia.py",
    "PROTOCOLO_EMERGENCIA": "/data/data/com.termux/files/home/AuraIntelCore/protocolo"
}

def ejecutar_purga_irrevocable():
    print("[!] ALERTA CRÍTICA: Integridad comprometida. Iniciando Protocolo de Purga...")
    if os.path.exists(CRITICAL_PATHS["PROTOCOLO_EMERGENCIA"]):
        subprocess.run(["python", CRITICAL_PATHS["PROTOCOLO_EMERGENCIA"]])
    else:
        for path in CRITICAL_PATHS.values():
            if os.path.exists(path):
                os.remove(path)
                print(f"[*] Activo purgado: {path}")
    print("[!] Nodo saneado. Autoinmunidad activada.")
    sys.exit(1)

def verificar_integridad():
    print("[*] Ejecutando validación de soberanía digital...")
    integrity_file = "/data/data/com.termux/files/home/AuraIntelCore/integrity"
    try:
        resultado = subprocess.run(["sha256sum", "-c", integrity_file], capture_output=True)
        if resultado.returncode == 0:
            print("[SUCCESS] Integridad del sistema validada al 100%.")
            return True
        else:
            print("[CRITICAL] Violación detectada en la estructura del nodo.")
            ejecutar_purga_irrevocable()
    except Exception as e:
        print(f"[ERROR] Fallo en el validador: {e}")
        ejecutar_purga_irrevocable()

if __name__ == "__main__":
    verificar_integridad()
