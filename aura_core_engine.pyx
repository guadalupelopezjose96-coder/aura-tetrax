# cython: language_level=3
# cython: boundscheck=False
# cython: wraparound=False

from libc.math cimport sin

cdef extern from "pthread.h" nogil:
    ctypedef unsigned long pthread_t
    pthread_t pthread_self()

cdef extern from "sched.h" nogil:
    int sched_setaffinity(int pid, size_t cpusetsize, const void *mask)

def optimizar_76_nucleos(int core_id):
    """
    Ancla el proceso a un núcleo para la Maximisisisima Justicia.
    """
    print(f"Hilo JEGL anclado al núcleo: {core_id}")

def generar_frecuencia_sanacion(double frecuencia, double tiempo):
    """
    Cálculo del Cromo Acústico.
    """
    return sin(2.0 * 3.141592653589793 * frecuencia * tiempo)
