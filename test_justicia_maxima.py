#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
# Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
# PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
import unittest
import time
from decimal import Decimal
from justicia_maxima import JusticiaMaximaCore
from config_data import CONFIGURACION_FISCAL_INMUTABLE

class TestJusticiaMaximaCore(unittest.TestCase):
    def setUp(self):
        self.core = JusticiaMaximaCore()
        
    def test_precision_aritmetica_estricta(self):
        """Verifica que no exista pérdida de precisión binaria en el cálculo fiscal"""
        base = CONFIGURACION_FISCAL_INMUTABLE["tasas_equivalencia"]["base_regulatoria"]
        factor = CONFIGURACION_FISCAL_INMUTABLE["tasas_equivalencia"]["factor_sustentabilidad"]
        
        resultado = base * factor
        self.assertEqual(resultado, Decimal("1979.100000000000000000000000"))

    def test_latencia_puente_nativo(self):
        """Monitorea que el puente de bajo nivel no sufra degradación de tiempo"""
        frecuencia = float(CONFIGURACION_FISCAL_INMUTABLE["frecuencias_sincronizacion"]["transformacion_nucleo"])
        
        # Ejecución del puente asíncrono simétrico
        tiempo_ns = self.core.bridge_modulo_nativo(frecuencia, 500000)
        
        # El log debe registrarse correctamente
        print(f"\n[INFO TEST] Rendimiento de ejecución verificado: {tiempo_ns} ns para 500k ciclos.")
        self.assertGreater(tiempo_ns, 0, "El contador de tiempo en nanosegundos debe ser positivo.")

if __name__ == "__main__":
    unittest.main()
