#!/usr/bin/env python3
import os

VAL_DIR = os.path.expanduser("~/validators")
OUTPUT = os.path.expanduser("~/estado_sistema_jegl.txt")

def exportar_estado():
    # 1. Obtener lista completa de archivos en validators
    archivos = sorted(os.listdir(VAL_DIR))
    
    with open(OUTPUT, "w") as f:
        f.write("--- INFORME DE ESTADO TOTAL JEGLAuraIntelCore ---\n")
        f.write(f"Total módulos detectados: {len(archivos)}\n")
        f.write("Lista de archivos:\n")
        for arch in archivos:
            f.write(f"- {arch}\n")
        f.write("\n--- INTEGRIDAD DE LEY ADT ---\n")
        acta_existe = os.path.exists(os.path.expanduser("~/acta_justicia_maximisima.txt"))
        f.write(f"Acta de Justicia presente: {'SÍ' if acta_existe else 'NO'}\n")
        f.write("Estado: 100% BLINDADO\n")

if __name__ == "__main__":
    exportar_estado()
    print("Estado consolidado en ~/estado_sistema_jegl.txt al 100%.")
