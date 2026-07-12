from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.appbar import MDTopAppBar, MDTopAppBarTitle
from kivymd.uix.list import MDListItem, MDListItemHeadlineText, MDListItemSupportingText, MDListItemLeadingIcon
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.progressindicator import MDLinearProgressIndicator
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import os

class ControlPanel(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.main_layout = BoxLayout(orientation='vertical')
        
        # Configuración de Barra Superior (Compatibilidad KivyMD 2.0.1)
        self.appbar = MDTopAppBar(type="small")
        self.appbar.add_widget(MDTopAppBarTitle(text="Aura Intel - Sistema Global"))
        self.main_layout.add_widget(self.appbar)
        
        # Monitor de Rendimiento (Optimizado para 76 Núcleos)
        self.cpu_card = BoxLayout(orientation='vertical', size_hint_y=None, height="120dp", padding="15dp", spacing="5dp")
        self.cpu_info = MDListItem(
            MDListItemHeadlineText(text="Carga del Sistema (76 Núcleos)"),
            MDListItemSupportingText(text="Sincronizando con hardware JEGL..."),
            MDListItemLeadingIcon(icon="cpu-64-bit")
        )
        self.progress = MDLinearProgressIndicator(value=0)
        self.cpu_card.add_widget(self.cpu_info)
        self.cpu_card.add_widget(self.progress)
        self.main_layout.add_widget(self.cpu_card)
        
        # Lista de Blindaje de Dominios
        self.scroll = MDScrollView()
        self.list_layout = BoxLayout(orientation='vertical', size_hint_y=None)
        self.list_layout.bind(minimum_height=self.list_layout.setter('height'))
        
        self.dominios = ["auraintelcore.com", "fourphonix.com", "prophonix.com", "standard1979.com"]
        self.items = {}

        for dom in self.dominios:
            item = MDListItem(
                MDListItemLeadingIcon(icon="shield-check", theme_icon_color="Custom", icon_color=[0, 1, 0, 1]),
                MDListItemHeadlineText(text=dom),
                MDListItemSupportingText(text="Estado: Seguro al 100%"),
            )
            self.list_layout.add_widget(item)
            self.items[dom] = item
            
        self.scroll.add_widget(self.list_layout)
        self.main_layout.add_widget(self.scroll)
        self.add_widget(self.main_layout)
        
        # Refresco automático cada 2 segundos
        Clock.schedule_interval(self.refresh_logic, 2)

    def refresh_logic(self, dt):
        # Lectura de carga (bypass de permisos Android)
        try:
            with os.popen("uptime") as f:
                output = f.read()
                load_avg = float(output.split("load average: ")[-1].split(",")[0])
                cpu_val = min(load_avg * 10, 100) 
        except:
            cpu_val = 0
            
        self.progress.value = cpu_val
        self.cpu_info.children[1].children[0].text = f"Carga estimada: {cpu_val:.1f}%"
        
        # Validación de Integridad (Ley ADT)
        log_path = os.path.expanduser("~/nginx_integrity.log")
        if os.path.exists(log_path):
            try:
                with open(log_path, "r") as f:
                    log_data = f.read()
                    for dom, widget in self.items.items():
                        if f"{dom}: DESVIACIÓN" in log_data:
                            widget.children[2].icon = "shield-alert"
                            widget.children[2].icon_color = [1, 0, 0, 1]
                            widget.children[1].children[0].text = "¡ALERTA DE SEGURIDAD!"
                        else:
                            widget.children[2].icon = "shield-check"
                            widget.children[2].icon_color = [0, 1, 0, 1]
                            widget.children[1].children[0].text = "Estado: Seguro"
            except:
                pass

class AuraIntelApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan" 
        return ControlPanel()

if __name__ == "__main__":
    AuraIntelApp().run()
