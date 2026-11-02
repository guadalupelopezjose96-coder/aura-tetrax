# SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
# Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
# PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.appbar import MDTopAppBar, MDTopAppBarTitle
from kivymd.uix.list import MDListItem, MDListItemHeadlineText, MDListItemSupportingText
from kivy.uix.boxlayout import BoxLayout
import os

class AuraPanel(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        
        # Corrección para KivyMD 2.0.1 (Captura 14069)
        self.bar = MDTopAppBar(type="small")
        self.bar.add_widget(MDTopAppBarTitle(text="Aura Intel Core - Justicia"))
        self.layout.add_widget(self.bar)
        
        # Monitor de Justicia (Evita error /proc/stat)
        self.info = MDListItem(
            MDListItemHeadlineText(text="Nodo: 192.168.1.124"),
            MDListItemSupportingText(text="Sincronía JEGL: Activa")
        )
        self.layout.add_widget(self.info)
        self.add_widget(self.layout)

class AuraApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"
        return AuraPanel()

if __name__ == "__main__":
    AuraApp().run()
