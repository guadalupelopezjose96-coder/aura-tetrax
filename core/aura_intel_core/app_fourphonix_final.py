# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

# COPYRIGHT: USPTO-JEGL-2026 - Propiedad Absoluta de la Federación Fourphonix
import stripe
import os
from flask import Flask, request, redirect, jsonify

app = Flask(__name__)

# LLAVE SECRETA DE OWNER (sk_live_...)
stripe.api_key = "mk_1TMahRFE1PknNS530rNyUoYd"

# --- MATRIZ DE PRECIOS DE RENTA MENSUAL ---
# Reemplace estos valores con los IDs de su Dashboard de Stripe
PHONIX_MASTER_PRICES = {
    'hexa': 'price_ID_HEXA_40',      # Renta $40.00
    'octa': 'price_ID_OCTA_88',      # Renta $88.00
    'dodeca': 'price_ID_DODECA_172', # Renta $172.00
    'icosa': 'price_ID_ICOSA_272_25' # Renta $272.25
}

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    lookup_key = request.form.get('lookup_key') # hexa, octa, dodeca o icosa

    try:
        # Iniciando sesión de cobro recurrente bajo Estándar 1979
        checkout_session = stripe.checkout.Session.create(
            line_items=[{
                'price': PHONIX_MASTER_PRICES.get(lookup_key),
                'quantity': 1,
            }],
            mode='subscription', # MODO RENTA ACTIVO
            success_url='https://fourphonix.com/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url='https://fourphonix.com/planes',
            subscription_data={
                'description': f'Acceso Soberano a Nodo {lookup_key.upper()} - FourPhonix',
            },
        )
        return redirect(checkout_session.url, code=303)
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == "__main__":
    # Puerto Áureo 1618 - Ignición de Búnker
    app.run(host='0.0.0.0', port=1618)
