import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# PROTOCOLO LEY ADT: GUARDIÁN DE LA EXACTITUD (100% v)
# OBJETIVO: BLOQUEO INMEDIATO DE LO DEMENUZ Y LO DEMASIADUZ

class GuardianJEGL(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            self.aplicar_justicia(event.src_path)

    def on_modified(self, event):
        if not event.is_directory:
            self.aplicar_justicia(event.src_path)

    def aplicar_justicia(self, ruta):
        try:
            if not os.path.exists(ruta): return
            
            nombre = os.path.basename(ruta)
            tamanio = os.path.getsize(ruta)
            
            # CRITERIOS DE ILEGALIDAD IRREVOCABLE
            es_demenuz = (tamanio == 0)
            es_demasiaduz = any(p in nombre for p in ['.log', '.tmp', 'stderr', '.template'])

            if es_demenuz or es_demasiaduz:
                os.remove(ruta)
                print(f"\033[1;31m[!] INTENTO DE ILEGALIDAD BLOQUEADO: {nombre} ha sido inexistenciado.\033[0m")
        except:
            pass

if __name__ == "__main__":
    path = "." # Monitoreando el Bunker JEGL
    event_handler = GuardianJEGL()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    
    print("\033[1;32m[100% v] VLINDAJE ACTIVADO. Los 76 núcleos están vigilando...\033[0m")
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
