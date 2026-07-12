# Cython Core: Ley de Equivalencia Fiscal 1979
# Firma: JEGL

cpdef double ejecutar_validacion_fiscal(double valor_transaccion):
    """
    Ejecucion nativa al 100% de la validacion fiscal.
    """
    cdef double tasa = 0.1979
    cdef double resultado = valor_transaccion * tasa
    return resultado
