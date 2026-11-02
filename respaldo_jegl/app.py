# SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
# Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
# PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

# app.py - Estatus: 100% v | Firma: J.E.G.L.
# Infraestructura Soberana para fourphonix.com

import os
import stripe
import csv
import psycopg2
from flask import Flask, render_template, request, jsonify, redirect, abort, send_from_directory
from functools import wraps
from dotenv import load_dotenv

# 1. Cargue de Vlindaje (Variables de Entorno)
load_dotenv()
app = Flask(__name__)

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET")

# Configuración de Base de Datos JEGL
DB_CONFIG = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5432")
}

# Lista Blanca de Soberanía (IPs Autorizadas)
IPS_AUTORIZADAS = ['127.0.0.1', 'tu_ip_local_aqui']

# --- DECORADORES DE JUSTICIA ---

def solo_jegl(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.remote_addr not in IPS_AUTORIZADAS:
            print(f"⚠️ Intento ilegal desde: {request.remote_addr}")
            abort(403)
        return f(*args, **kwargs)
    return decorated_function

# --- LÓGICA DE NEGOCIO ---

def buscar_precio(nombre_producto):
    try:
        with open('prices.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['name'] == nombre_producto:
                    return row['price_id'], int(row['price_amount'])
    except FileNotFoundError:
        print("❌ Error: prices.csv no encontrado.")
    return None, None

def registrar_venta_sql(producto, monto):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO registros_plusvalia (producto_nombre, monto_centavos)
            VALUES (%s, %s);
        """, (producto, monto))
        conn.commit()
        cur.close()
        conn.close()
        print(f"✅ Plusvalía registrada: {producto}")
    except Exception as e:
        print(f"❌ Error SQL: {e}")

# --- RUTAS DE IGNICIÓN ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sw.js')
def service_worker():
    return send_from_directory('.', 'sw.js', mimetype='application/javascript')

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    # Soporte dual: JSON y Formulario Legal
    product_name = request.form.get('product_name') or request.json.get('product_name')
    price_id, _ = buscar_precio(product_name)

    if not price_id:
        return jsonify(error="Producto inexistenciado"), 404

    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[{'price': price_id, 'quantity': 1}],
            mode='payment',
            success_url='https://fourphonix.com/success',
            cancel_url='https://fourphonix.com/cancel',
            metadata={'product_name': product_name}
        )
        return redirect(checkout_session.url, code=303)
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route('/dashboard-jegl')
@solo_jegl
def dashboard():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        cur.execute("SELECT SUM(monto_centavos), COUNT(*) FROM registros_plusvalia;")
        res = cur.fetchone()
        total_usd = (res[0] or 0) / 100.0
        igniciones = res[1] or 0
        cur.close()
        conn.close()
        return render_template('dashboard.html', total_usd=f"{total_usd:,.2f}", igniciones=igniciones)
    except Exception as e:
        return f"Error de Búnker: {e}", 500

@app.route('/webhook', methods=['POST'])
def webhook():
    payload = request.get_data()
    sig_header = request.headers.get('STRIPE_SIGNATURE')
    try:
        event = stripe.Webhook.construct_event(payload, sig_header, WEBHOOK_SECRET)
    except Exception:
        return jsonify(success=False), 400

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        registrar_venta_sql(session['metadata']['product_name'], session['amount_total'])

    return jsonify(success=True)

if __name__ == '__main__':
    # Ignición en puerto 8080 para Termux/Samsung A16
    app.run(host='0.0.0.0', port=8080, debug=False)
