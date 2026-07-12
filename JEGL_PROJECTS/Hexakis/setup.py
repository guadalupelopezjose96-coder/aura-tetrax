# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

from setuptools import setup, Extension
from Cython.Build import cythonize

ext_modules = [
    Extension(
        "mercado_estandar",
        sources=["src/core/mercado_estandar.pyx"],
        extra_compile_args=['-O3', '-march=native'],
    )
]

setup(
    name="AuraIntelCore_Engine",
    ext_modules=cythonize(ext_modules, compiler_directives={'language_level': "3"}),
    zip_safe=False,
)

