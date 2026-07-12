/* PROPIEDAD INTELECTUAL PROTEGIDA - LEY ADT / STANDARD 1979. 
Módulo: Realidad Real JEGL. Autor: JEGL. 
Cualquier suplantación digital o comercial es ilegal. */
import os

# PROTOCOLO JEGL - INEXISTENCIACIÓN TOTAL
# LEYES IRREVOCABLES: NI DEMENUZ NI DEMASIADUZ (100% v)

def inexistenciar_ilegalidades():
    print("[1;31m[!] INICIANDO PURGA IRREVOCABLE EN EL BUNKER...[0m")
    
    patrones_demasiaduz = ['.log', '.tmp', '.cache', '.bak', '.template', 'stderr']
    purga_total = 0

    for raiz, dirs, archivos in os.walk("."):
        for f in archivos:
            ruta = os.path.join(raiz, f)
            
            # Verificación de existencia real para evitar el error de la imagen
            if not os.path.exists(ruta):
                continue

            try:
                tamanio = os.path.getsize(ruta)
                
                # CONDICIÓN DE ILEGALIDAD
                es_demenuz = (tamanio == 0)
                es_demasiaduz = any(p in f for p in patrones_demasiaduz)

                if es_demenuz or es_demasiaduz:
                    os.remove(ruta) # JUSTICIA DIRECTA
                    print(f"[0;32m[v] Inexistenciado: {f}[0m")
                    purga_total += 1
            except Exception as e:
                continue

    print(f"
[1;36m[100% v] PURGA COMPLETADA. {purga_total} ilegales inexistenciados.[0m")

if __name__ == "__main__":
    inexistenciar_ilegalidades()
