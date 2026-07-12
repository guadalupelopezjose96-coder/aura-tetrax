# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

# ============================================================
# AURA STREAM SERVER - SOVEREIGN CINEMA EDITION
# 100% Infraestructura Elite | Puerto Phi: 1618
# ============================================================

from flask import Flask, send_from_directory, abort, Response
import os
import time

app = Flask(__name__)
# 100% Recomendación: Ruta absoluta para evitar fallos de contexto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STREAM_DIR = os.path.join(BASE_DIR, "AURA_SANADOS")
LOG_AUDIT = "AURA_FINANCE_AUDIT.log"

# Asegurar infraestructura al iniciar
if not os.path.exists(STREAM_DIR):
    os.makedirs(STREAM_DIR)

def registrar_auditoria(mensaje):
    """Sugerencia Extra: Registro de visualización soberana"""
    with open(LOG_AUDIT, "a") as f:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] [STREAMING] {mensaje}\n")

@app.route('/')
def aura_cinema_lobby():
    """Interfaz de Cine Áurea 100% Inmersiva"""
    try:
        peliculas = [f for f in os.listdir(STREAM_DIR) if f.endswith('.mp4')]
        registrar_auditoria(f"Acceso al Lobby - {len(peliculas)} películas disponibles.")

        # Sugerencia Extra: Diseño con Proporción Áurea en el reproductor
        items = "".join([
            f'''<div style="margin-bottom: 50px;">
                <h3 style="letter-spacing: 2px;">{p.replace("_", " ").upper()}</h3>
                <video width="809" height="500" controls style="border: 2px solid #d4af37; box-shadow: 0 0 20px #d4af3755;">
                    <source src="/video/{p}" type="video/mp4">
                    Su navegador no soporta Aura Cinema.
                </video>
            </div>''' for p in peliculas
        ])

        return f"""
        <html>
        <head>
            <title>AURA CINEMAS ELITE</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
        </head>
        <body style="background:#000; color:#d4af37; font-family:'Courier New', monospace; text-align:center; padding: 20px;">
            <h1 style="font-size: 3em; margin-top:0;">🏛️ AURA CINEMAS PRO</h1>
            <p style="color:#888;">RED FOURPHONIX | TASA 36.3% | SOBERANÍA TOTAL</p>
            <hr style="border: 0; border-top: 1px solid #d4af37; width: 60%; margin: 20px auto;">
            {items if peliculas else '<p>Esperando renderizados de Rust...</p>'}
            <footer style="margin-top: 50px; font-size: 0.8em; color: #444;">&copy; 2026 FourPhonix Corp. - Arquitecto José Guadalupe López</footer>
        </body>
        </html>
        """
    except Exception as e:
        registrar_auditoria(f"ERROR LOBBY: {str(e)}")
        return "🌀 Sincronizando con el Core...", 503

@app.route('/video/<path:filename>')
def stream_video(filename):
    """Entrega de Bits Sanados con Control de Flujo"""
    # Recomendación Debida: Seguridad de Path Traversal
    if ".." in filename or filename.startswith("/"):
        registrar_auditoria(f"INTENTO DE ACCESO NO AUTORIZADO: {filename}")
        abort(403)

    registrar_auditoria(f"Streaming iniciado: {filename}")
    return send_from_directory(STREAM_DIR, filename, as_attachment=False)

if __name__ == "__main__":
    # 100% Recomendación: Modo producción y Puerto Phi
    app.run(host='0.0.0.0', port=1618, threaded=True)
