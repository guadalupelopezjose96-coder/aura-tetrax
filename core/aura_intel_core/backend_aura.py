# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

# COPYRIGHT: USPTO-JEGL-2026 - Propiedad Absoluta de la Federación Fourphonix

import stripe
from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

# LLAVE SECRETA DE OWNER
stripe.api_key = "sk_live_TU_LLAVE_AQUI"

@app.route('/webhook-pago-exitoso', methods=['POST'])
def webhook():
    payload = request.get_data()
    sig_header = request.headers.get('Stripe-Signature')

    try:
        # Verificación de la señal de capital
        event = stripe.Webhook.construct_event(
            payload, sig_header, "whsec_TU_WEBHOOK_SECRET"
        )

        if event['type'] == 'checkout.session.completed':
            session = event['data']['object']
            nivel = session.get('metadata', {}).get('phonix_type', 'hexa')

            print(f"--- CAPITAL CONFIRMADO: ACTIVANDO {nivel.upper()} ---")

            # IGNICIÓN AUTOMÁTICA DEL MOTOR AURA (Rust/FFmpeg)
            # Se asignan los hilos según el nivel pagado ($40 - $272.25)
            comando_saneamiento = f"./ignicion_aura.sh --nivel {nivel} --tasa 0.363"
            subprocess.Popen(comando_saneamiento, shell=True)

            return jsonify(status="Motor Aura Encendido"), 200

    except Exception as e:
        return jsonify(error=str(e)), 400

if __name__ == "__main__":
    # Puerto de Saneamiento
    app.run(host='0.0.0.0', port=1979)
