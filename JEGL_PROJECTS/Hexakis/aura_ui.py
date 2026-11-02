# SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
# Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
# PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.clock import Clock
import mercado_estandar  # Importa tu binario .so

class AuraInterface(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.layout = MDBoxLayout(orientation='vertical', padding=30, spacing=25)
        
        # Encabezado con Firma JEGL
        self.header = MDLabel(
            text="AURA INTEL CORE\n[ PROTOCOLO SOBERANO 1979 ]",
            halign="center",
            font_style="Display", # Estilo actualizado
            role="medium",
            theme_text_color="Primary"
        )
        
        self.status = MDLabel(
            text="RESONANCIA: 528Hz | ESTADO: ACTIVO",
            halign="center",
            theme_text_color="Secondary",
            font_style="Label",
            role="large"
        )

        self.result_display = MDLabel(
            text="0.00",
            halign="center",
            font_style="Display",
            role="large",
            theme_text_color="Custom",
            text_color=(0, 0.8, 1, 1) # Azul Eléctrico Aura
        )

        # Botón con nueva sintaxis KivyMD 2.0
        self.btn = MDButton(
            MDButtonText(text="EJECUTAR VALIDACIÓN FISCAL"),
            style="filled",
            pos_hint={"center_x": .5},
            on_release=self.procesar_ley
        )
        
        self.layout.add_widget(self.header)
        self.layout.add_widget(self.status)
        self.layout.add_widget(self.result_display)
        self.layout.add_widget(self.btn)
        self.add_widget(self.layout)

    def procesar_ley(self, *args):
        # Ejecuta la lógica del binario compilado
        monto_prueba = 1000.0
        calculo = mercado_estandar.ejecutar_validacion_fiscal(monto_prueba)
        self.result_display.text = f"Equivalencia: {calculo:.4f}"

class AuraApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan" # Color Aura Intel
        return AuraInterface()

if __name__ == "__main__":
    AuraApp().run()
