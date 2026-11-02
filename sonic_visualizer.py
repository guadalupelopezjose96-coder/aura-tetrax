# SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
# Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
# PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

from kivy.uix.widget import Widget
from kivy.graphics import Color, Line
from kivy.clock import Clock

class SonicVisualizer(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.points = []
        # Actualización a 60 FPS para máxima fluidez
        Clock.schedule_interval(self.update_canvas, 1/60)

    def update_data(self, audio_buffer):
        """ Recibe el buffer del bridge de C++ """
        # Convertimos los datos de amplitud en coordenadas Y para la pantalla
        # Normalizamos el 100% del espectro visible
        self.points = []
        width_step = self.width / len(audio_buffer)

        for i, amplitude in enumerate(audio_buffer):
            x = self.x + (i * width_step)
            y = self.center_y + (amplitude * self.height / 2)
            self.points.extend([x, y])

    def update_canvas(self, dt):
        self.canvas.clear()
        with self.canvas:
            Color(0, 1, 0.8, 1)  # Color "Aura" (Cian/Verde)
            if len(self.points) > 4:
                Line(points=self.points, width=1.5, joint='round')
