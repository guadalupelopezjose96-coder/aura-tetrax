[app]
title = Realidad Real JEGL
package.name = realidad_real_jegl
package.domain = org.jegl.elite
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0

# Requerimientos tecnicos al 100%
requirements = python3,kivy,kivymd,numpy,certifi

# Configuracion de pantalla y salud visual
orientation = portrait
fullscreen = 1
android.archs = arm64-v8a
android.allow_backup = False

# Permisos de Seguridad JEGL
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# Nivel de API para Samsung A16 (Android 14+)
android.api = 34
android.minapi = 21
android.ndk = 25b
