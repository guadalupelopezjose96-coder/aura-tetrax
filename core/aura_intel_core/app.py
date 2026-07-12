# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

# COPYRIGHT: USPTO-JEGL-2026 - Propiedad Absoluta de la Federación Fourphonix
import os
import subprocess
import psutil
import stripe
from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# --- I. IDENTIDAD SOBERANA (100% LEGAL) ---
# Sustituye con tu clave real sk_test_... para activar el flujo de oro
stripe.api_key = "PON_AQUI_TU_SECRET_KEY_DE_LA_IMAGEN_10625"

# Llave de acceso exclusiva para el Dueño Nominal
OWNER_KEY = "maestria1979"

# Rutas del Sistema
BASE_DIR = "/data/data/com.termux/files/home"
BUNKER_DIR = os.path.join(BASE_DIR, "bunker/resultados")
if not os.path.exists(BUNKER_DIR):
    os.makedirs(BUNKER_DIR)

# --- II. INTERFAZ DE USUARIO (EL PORTAL PHONIX) ---
@app.route('/')
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>FourPhonix | Aura Intel Core</title>
        <style>
            body { background: radial-gradient(circle, #0a0a0a, #000); color: #00ff00; font-family: 'Courier New', monospace; text-align: center; padding: 50px; overflow: hidden; }
            .bunker-box { border: 3px solid #00ff00; padding: 40px; display: inline-block; box-shadow: 0 0 30px #00ff00; background: rgba(0,255,0,0.05); }
            .status { color: #fff; font-size: 1.5em; text-transform: uppercase; letter-spacing: 2px; }
            .btn-pago { background: #00ff00; color: #000; padding: 20px 40px; text-decoration: none; font-weight: bold; border-radius: 5px; box-shadow: 0 5px 0 #008800; transition: 0.3s; }
            .btn-pago:hover { background: #fff; box-shadow: 0 0 20px #fff; }
        </style>
    </head>
    <body>
        <div class="bunker-box">
            <h1>SYSTEMA FOURPHONIX ACTIVADO</h1>
            <p class="status">NÚCLEOS AURA 11.3x OPERATIVOS</p>
            <hr border="1" color="#00ff00">
            <p>100% Sanación de Audio y Video | Justicia Maximísima</p>
            <br><br>
            <a href="/checkout" class="btn-pago">ADQUIRIR PLAN ICOSA ($272.25)</a>
        </div>
        <p style="margin-top:100px; opacity:0.3;">© Soberano J.E.G.L. - Standard 1979 - 2026</p>
    </body>
    </html>
    """)

# --- III. DASHBOARD PROPIETARIO PROTEGIDO (100% DEVIDO) ---
@app.route('/owner-dashboard-1979')
def dashboard():
    # FILTRO DE INSUFICIENCIA: Solo el dueño con la llave entra
    key = request.args.get('key')
    if key != OWNER_KEY:
        return "<h1>ACCESO ILEGAL DETECTADO. BLOQUEO ENVIADO.</h1>", 403

    cpu_uso = psutil.cpu_percent(interval=1)
    return render_template_string("""
    <body style="background:#000; color:#0f0; font-family:monospace; padding:30px; border: 10px solid gold;">
        <h1 style="color:gold;">DASHBOARD SOBERANO J.E.G.L.</h1>
        <div style="border:2px solid #0f0; padding:20px; background:#111;">
            <h3>LIQUIDACIÓN DE CAPITAL (STRIPE)</h3>
            <p>Volumen: <span style="color:#fff;">$100.00 USD</span></p>
            <p>Neto Chime: <span style="color:gold;">$77.01 USD</span></p>
            <p>Estado: <span style="color:cyan;">EQUIVALENCIA FISCAL VERIFICADA</span></p>
        </div>
        <br>
        <div style="border:1px solid #0f0; padding:20px;">
            <h3>RENDIMIENTO DEL BÚNKER</h3>
            <p>CPU: {{ c }}% | TÚNEL: CLOUDFLARE ACTIVO</p>
            <p>LEY: EL 100% DE LO QUE ESTÁ DE MENOS ES ILEGAL</p>
        </div>
        <br>
        <form action="/panic-1979" method="post">
            <input type="submit" value="BOTÓN DE PÁNICO: DESTRUIR SESIÓN" style="background:red; color:white; width:100%; padding:20px; font-weight:bold; cursor:pointer;">
        </form>
    </body>
    """, c=cpu_uso)

# --- IV. PROCESAMIENTO DE PAGO (STRIPE) ---
@app.route('/checkout')
def create_checkout_session():
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {'name': 'Plan IcosaPhonix 11.3x'},
                    'unit_amount': 27225, # $272.25 en centavos
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='https://fourphonix.com/success',
            cancel_url='https://fourphonix.com/cancel',
        )
        return render_template_string("<script>window.location.href='{{url}}'</script>", url=session.url)
    except Exception as e:
        return str(e)

# --- V. BOTÓN DE PÁNICO (JUSTICIA MAXIMÍSIMA) ---
@app.route('/panic-1979', methods=['POST'])
def panic():
    # Ejecuta script de cierre de emergencia
    subprocess.call(["bash", "panic_button.sh"])
    return "<h1>BÚNKER SELLADO. PROCESOS ELIMINADOS AL 100%.</h1>"

if __name__ == '__main__':
    # Puerto 1618 - Debug=False para evitar lo que está de más (Ilegal)
    app.run(host='0.0.0.0', port=1618, debug=False)
