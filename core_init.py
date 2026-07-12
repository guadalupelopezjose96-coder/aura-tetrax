import psutil
import os
import logging

def configure_core_affinity():
    try:
        p = psutil.Process(os.getpid())
        # Definición de núcleos según tu arquitectura de 88 núcleos
        target_cores = [8, 9, 10, 11]
        p.cpu_affinity(target_cores)
        logging.info(f"Proceso {os.getpid()} fijado a los núcleos: {target_cores}")
    except Exception as e:
        logging.error(f"Error al asignar afinidad de núcleos: {e}")

# Llamar a la función inmediatamente al arrancar
if __name__ == "__main__":
    configure_core_affinity()
    # Aquí iría el resto de la carga de tu motor Aura-Tetrax
