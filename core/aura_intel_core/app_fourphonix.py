# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

# COPYRIGHT: USPTO-JEGL-2026 - Propiedad Absoluta de la Federación Fourphonix
import stripe
import os
import subprocess
from flask import Flask, render_template, request, redirect, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)

# --- CONFIGURACIÓN DE PROPIETARIO ---
# Actualizar con sk_live_ tras el pago de Google Workspace
stripe.api_key = os.getenv("STRIPE_KEY", "sk_test_tu_llave_maestra")

CORS(app, origins=["https://fourphonix.com", "https://auraintelcore.com"])

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AURA_STORAGE = os.path.join(BASE_DIR, 'AURA_VENTAS')
os.makedirs(AURA_STORAGE, exist_ok=True)

# --- MATRIZ DE RENTA MENSUAL PHONIX ---
@app.route('/create-subscription', methods=['POST'])
def create_subscription():
    lookup_key = request.form.get('lookup_key')
    # IDs de productos creados en su Dashboard de Stripe
    prices = {
        'hexa': 'price_HEXA_ID',     # $40.00/mes
        'octa': 'price_OCTA_ID',     # $88.00/mes
        'dodeca': 'price_DODECA_ID', # $172.00/mes
        'icosa': 'price_ICOSA_ID'    # $272.25/mes
    }

    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[{'price': prices[lookup_key], 'quantity': 1}],
            mode='subscription',
            payment_method_types=['card'],
            invoice_creation={'enabled': True},
            success_url='https://fourphonix.com/bunker?pago=exitoso&session_id={CHECKOUT_SESSION_ID}',
            cancel_url='https://fourphonix.com/planes',
        )
        return redirect(checkout_session.url, code=303)
    except Exception as e:
        return jsonify(error=str(e)), 500

# --- NODO PHONIX (Y): MOTOR DE ALQUIMIA SANEADO ---
@app.route('/alquimia', methods=['POST'])
def process_audio():
    # Parámetros validados en el stress-test exitoso de hoy
    input_file = request.files['file']
    output_name = f"SANEADO_SOBERANO_{os.urandom(4).hex()}.mp4"
    output_path = os.path.join(AURA_STORAGE, output_name)
    input_file.save("temp.mp4")

    # Sintaxis Maestra 36.3% validada en libavfilter 11.14.100
    cmd = (
        f"ffmpeg -y -i temp.mp4 -f lavfi -i 'anoisesrc=a=0.363:d=30' "
        f"-filter_complex '[0:a][1:a]amix=inputs=2:duration=first' "
        f"-c:a aac -b:a 320k {output_path}"
    )
    subprocess.run(cmd, shell=True)
    return send_from_directory(AURA_STORAGE, output_name)

if __name__ == "__main__":
    # Puerto de la Proporción Áurea (1.618)
    app.run(host='0.0.0.0', port=1618)
