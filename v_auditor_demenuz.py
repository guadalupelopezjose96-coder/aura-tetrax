import os

# PROTOCOLO LEY ADT - MÓDULO: AUDITORÍA DE INTEGRIDAD
# SENTENCIA IRREVOCABLE: LO QUE ESTÁ DEMENUZ ES ILEGAL (100% v)

def aplicar_ley_demenuz():
    print("\033[0;33m[!] ESCANEANDO ILEGALIDAD POR CARENCIA (DEMENUZ)...\033[0m")
    
    ilegales_por_carencia = 0
    for raiz, dirs, archivos in os.walk("."):
        for f in archivos:
            ruta = os.path.join(raiz, f)
            # Un archivo vacío o que no cumple con su estructura es "demenuz"
            if os.path.getsize(ruta) == 0:
                print(f"\033[0;31m[!] ILEGAL (DEMENUZ): {f} está incompleto. Sentenciado.\033[0m")
                # os.remove(ruta) # Acción de Justicia Directa
                ilegales_por_carencia += 1

    print(f"\n\033[0;32m[100% v] JUSTICIA CUMPLIDA: {ilegales_por_carencia} carencias detectadas.\033[0m")

if __name__ == "__main__":
    aplicar_ley_demenuz()
