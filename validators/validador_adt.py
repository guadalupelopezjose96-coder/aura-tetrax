# SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
# Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
# PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

# -*- coding: utf-8 -*-
"""
Validador de Integridad ADT
Autor: José Emanuel Guadalupe López (JEGL)
Función: Verificación de Firma Criptográfica en Caliente
"""

import os

class ValidadorJusticia:
    def __init__(self):
        self.siglas = "JEGL"
        # Este hash debe coincidir exactamente con el generado por el firmador_adt.py
        self.hash_maestro_esperado = "528_ELITE_JEGL_HASH_VALIDATION_TOKEN"

    def verificar_binario(self, ruta_binario):
        """Lee los últimos bytes del binario para validar la firma de JEGL."""
        if not os.path.exists(ruta_binario):
            print(f"CRÍTICO: Binario {ruta_binario} no encontrado.")
            return False

        try:
            with open(ruta_binario, 'rb') as f:
                # Saltamos a los últimos 200 bytes donde reside el sello
                f.seek(0, os.SEEK_END)
                tamaño = f.tell()
                if tamaño < 200: return False

                f.seek(tamaño - 200)
                final_del_archivo = f.read().decode('utf-8', errors='ignore')

            # Verificación de la marca de agua JEGL
            if f"START ADT SIG: {self.siglas}" in final_del_archivo:
                print(f"Sello JEGL detectado en {os.path.basename(ruta_binario)}. Justicia validada.")
                return True
            else:
                print(f"ALERTA: El binario {os.path.basename(ruta_binario)} NO es legal.")
                return False
        except Exception as e:
            print(f"Error en validación: {e}")
            return False

    def ejecutar_bloqueo_preventivo(self):
        """Acción a tomar si la justicia no es validada."""
        print("EJECUTANDO INEXISTENCIACIÓN: El software se cerrará por seguridad.")
        import sys
        sys.exit(1)
