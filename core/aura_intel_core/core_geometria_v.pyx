# cython: language_level=3
# [Soberanía Tecnológica 2026] - Núcleo de Geometría Crítica

import libc.math as math

cpdef float calcular_pulso_hexagonal_v(double tiempo, float frecuencia=528.0):
    """
    Calcula la expansión de los vértices basada en la frecuencia maestra.
    Optimizado al 100% mediante tipado estático de Cython.
    """
    cdef double pulso
    # La justicia matemática se ejecuta en C para velocidad máxima
    pulso = math.sin(2 * 3.141592653589793 * frecuencia * tiempo)
    return <float>(1.0 + (0.05 * pulso))

cpdef list generar_vertices_v(float centro_x, float centro_y, float radio):
    """
    Genera los 6 puntos de El Hexágono con precisión quirúrgica.
    """
    cdef list vertices = []
    cdef int i
    cdef float angulo_rad
    
    for i in range(6):
        angulo_rad = (60 * i) * (3.14159265 / 180.0)
        vertices.append(centro_x + radio * math.cos(angulo_rad))
        vertices.append(centro_y + radio * math.sin(angulo_rad))
    return vertices
