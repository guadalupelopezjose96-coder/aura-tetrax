/* PROPIEDAD INTELECTUAL PROTEGIDA - LEY ADT / STANDARD 1979. 
Módulo: Realidad Real JEGL. Autor: JEGL. 
Cualquier suplantación digital o comercial es ilegal. */
import numpy as np
import simpleaudio as sa

# =================================================================
# AURA INTEL - RÁFAGA SÓNICA 528Hz (NOTIFICACIÓN)
# PROTOCOLO: MAXIMISISISIMA JUSTICIA / STANDARD 1979
# =================================================================

def disparar_528hz(duracion=0.5):
    frecuencia = 528
    fs = 44100
    t = np.linspace(0, duracion, int(fs * duracion), False)
    
    # Generación de la onda de sanación
    onda = np.sin(frecuencia * t * 2 * np.pi)
    audio = (onda * 32767 / np.max(np.abs(onda))).astype(np.int16)
    
    # Reproducción inmediata
    play_obj = sa.play_buffer(audio, 1, 2, fs)
    play_obj.wait_done()

if __name__ == "__main__":
    disparar_528hz()
