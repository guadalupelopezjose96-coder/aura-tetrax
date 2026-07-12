# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

import csv

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    # Buscamos el ID en tu archivo prices.csv de forma soberana
    with open('prices.csv', mode='r') as file:
        reader = csv.DictReader(file)
        # Filtramos por el Hexaphonix 3D Alpha
        product = next(row for row in reader if row['product_name'] == 'Hexaphonix 3D Alpha')

    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[{
                'price': product['price_id'], # ID legal del CSV
                'quantity': 1,
            }],
            mode='payment',
            success_url=f"http://{BASE_URL}/success",
            cancel_url=f"http://{BASE_URL}/cancel",
        )
        return jsonify({'url': checkout_session.url})
    except Exception as e:
        return jsonify(error=str(e)), 403

