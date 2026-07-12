import os
import time
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# PROTOCOLO LEY ADT: GUARDIÁN CON ALERTA DE SELLO (100% v)
# SENTENCIA: NOTIFICACIÓN Y ANIQUILACIÓN AL MICROSEGUNDO

class GuardianAlertaJEGL(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            self.ejecutar_sentencia(event.src_path)

    def ejecutar_sentencia(self, ruta):
        try:
            if not os.path.exists(ruta): return
            
            nombre = os.path.basename(ruta)
            tamanio = os.path.getsize(ruta)
            
            # CRITERIOS DE ILEGALIDAD JEGL
            es_demenuz = (tamanio == 0)
            es_demasiaduz = any(p in nombre for p in ['.log', '.tmp', 'stderr', '.template', '.tmpl', '.gitkeep'])

            if es_demenuz or es_demasiaduz:
                os.remove(ruta)
                # ALERTA DE SELLO: Mensaje brillante + Sonido de sistema (\a)
                sys.stdout.write("\a") 
                sys.stdout.flush()
                print(f"\033[1;33m[!] ALERTA DE SELLO: Intento de Ilegalidad detectado en '{nombre}'.\033[0m")
                print(f"\033[1;31m[v] SENTENCIA: Inexistenciación Total completada al 100%.\033[0m\n")
        except:
            pass

if __name__ == "__main__":
    path = "." 
    event_handler = GuardianAlertaJEGL()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    
    print("\033[1;36m[BUNKER JEGL] VLINDAJE CON ALERTA ACTIVADO.\033[0m")
    print("\033[1;32mEscuchando la Realidad Real... El 100% de lo ilegal será borrado.\033[0m\n")
    
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
