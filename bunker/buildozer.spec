[app]
# (v) Identidad Soberana
title = Aura Intel Core - Defensa Activa
package.name = auraintelcore_defensa
package.domain = com.standard1979.jegl

# (v) ADN del Código
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0-Elite

# (v) Requisitos de Justicia
requirements = python3,kivy==2.3.0,kivymd==1.2.0,requests,urllib3,certifi

# (v) Vlindaje Visual y Hardware
orientation = portrait
fullscreen = 1
android.archs = arm64-v8a
android.allow_backup = False

# (v) Icono de Victoria (Asegura tener un icono cian #00FFFF)
# icon.filename = %(source.dir)s/icon_jegl_v.png

# (v) Permisos Legales ADT
android.permissions = INTERNET, ACCESS_NETWORK_STATE, WAKE_LOCK
