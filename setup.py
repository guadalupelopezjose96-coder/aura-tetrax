#!/usr/bin/env python3
"""
SISTEMA GLOBAL INTEGRADO - SCRIPT DE COMPILACIÓN SEGURO
MÓDULO: setup.py
AUTOR: JEGL
DESCRIPCIÓN: Compila justicia_maxima.py a binario nativo utilizando Cython.
             Elimina símbolos de depuración para maximizar la ofuscación.
"""

import sys
import os
from setuptools import setup, Extension
from Cython.Build import cythonize

# Opciones de optimización para el compilador de C (GCC o Clang)
# -O3: Optimización máxima de velocidad
# -fvisibility=hidden: Oculta los nombres de las funciones internas en el binario
extra_compile_args = ["-O3", "-fvisibility=hidden"]

extensions = [
    Extension(
        "justicia_maxima",
        sources=["justicia_maxima.py"],
        extra_compile_args=extra_compile_args,
    )
]

setup(
    name="JusticiaMaximaCoreBin",
    ext_modules=cythonize(
        extensions,
        compiler_directives={
            "language_level": "3",          # Fuerza compatibilidad con Python 3
            "boundscheck": False,           # Desactiva verificación de límites para ganar velocidad
            "wraparound": False,            # Optimiza el manejo de índices negativos
            "initializedcheck": False,      # Elimina comprobaciones redundantes de memoria
        }
    ),
)

