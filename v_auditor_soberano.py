/* PROPIEDAD INTELECTUAL PROTEGIDA - LEY ADT / STANDARD 1979. 
Módulo: Realidad Real JEGL. Autor: JEGL. 
Cualquier suplantación digital o comercial es ilegal. */
import multiprocessing as mp
import os
import hashlib
import time

# Configuración JEGL - Standard 1979
THREADS = 76
DIRECTORIO_AUDITORIA = "./"

def calcular_hash_archivo(ruta_archivo):
    """Calcula el hash SHA-256 de un archivo para el Sello ADT."""
    sha256_hash = hashlib.sha256()
    try:
        with open(ruta_archivo, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return (ruta_archivo, sha256_hash.hexdigest())
    except Exception as e:
        return (ruta_archivo, f"Error: {str(e)}")

def auditoria_soberana():
    print(f"--- Iniciando Auditoría Soberana JEGL (76 Núcleos) ---")
    
    # 1. Escanear archivos (excluyendo .git y carpetas pesadas)
    archivos = []
    for raiz, dirs, ficheros in os.walk(DIRECTORIO_AUDITORIA):
        if '.git' in dirs: dirs.remove('.git')
        for f in ficheros:
            archivos.append(os.path.join(raiz, f))

    print(f"[+] Archivos detectados: {len(archivos)}")
    print(f"[+] Desplegando auditoría en {THREADS} hilos...")

    inicio = time.time()

    # 2. PROCESAMIENTO PARALELO (El núcleo de Aura Intel Core)
    with mp.Pool(processes=THREADS) as pool:
        resultados = pool.map(calcular_hash_archivo, archivos)

    fin = time.time()

    # 3. Guardar resultados en el Sello ADT
    with open("v_sello_adt_total.txt", "w") as f_out:
        f_out.write(f"REPORTE DE SOBERANÍA DIGITAL - {time.ctime()}
")
        f_out.write(f"Tiempo de ejecución: {fin - inicio:.4f} segundos
")
        f_out.write("-" * 50 + "
")
        for ruta, hash_res in resultados:
            f_out.write(f"{ruta}: {hash_res}
")

    print(f"--- Auditoría Completada en {fin - inicio:.2f}s ---")
    print(f"[!] Reporte generado en: v_sello_adt_total.txt")

if __name__ == "__main__":
    auditoria_soberana()
