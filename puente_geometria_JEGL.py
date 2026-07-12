# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

# =================================================================
# PUENTE SOBERANO: puente_geometria_JEGL.py
# ARQUITECTO: José Emanuel Guadalupe López (JEGL)
# =================================================================
import ctypes
import os

class GeometriaSagradaJEGL:
    def __init__(self):
        ruta = os.path.abspath("./core_modules/geometria_sagrada.so")
        self.lib = ctypes.CDLL(ruta)

        # Definir tipos de datos para precisión v
        self.lib.frecuencia_armonica_jegl.restype = ctypes.c_float
        self.lib.calcular_posicion_hexagonal_v.restype = ctypes.c_float

    def obtener_frecuencia_v(self, vertices=6):
        """Retorna la frecuencia basada en el Hexágono JEGL."""
        return self.lib.frecuencia_armonica_jegl(vertices)

    def mapear_red_soberana(self, x, y):
        """Calcula la posición en la malla geométrica."""
        return self.lib.calcular_posicion_hexagonal_v(ctypes.c_float(x), ctypes.c_float(y))
