# SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
# Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
# PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

# ############################################################# #
# #            SISTEMA DE MANDO REMOTO Y SOBERANÍA            # #
# #            PROPIEDAD INTELECTUAL PRIVADA JEGL             # #
# ############################################################# #

import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Llave de Validación de Justicia Maximisisisima
SECRET_KEY_V = os.getenv("JEGL_MASTER_KEY")

@app.route('/ejecutar_v', methods=['POST'])
def ejecutar_comando():
    data = request.json
    key = data.get('key')
    comando = data.get('comando')

    # 1. Filtro de Excelencia (Validación de Identidad)
    if key != SECRET_KEY_V:
        return jsonify({"status": "ACCESO ILEGAL - INEXISTENCIADO"}), 403

    # 2. Ejecución de Órdenes de Soberanía
    if comando == "REINICIAR_NODOS":
        os.system("v_update_all") # Tu script de triple enlace
        return jsonify({"status": "v", "msg": "Triple Enlace Reiniciado"}), 200

    elif comando == "LIMPIEZA_TOTAL":
        os.system("v_limpieza_raiz")
        return jsonify({"status": "v", "msg": "Espectros Inexistenciados"}), 200

    return jsonify({"status": "error", "msg": "Comando no reconocido"}), 400

if __name__ == "__main__":
    # Escuchando en el puerto de mando 8888
    app.run(host='0.0.0.0', port=8888)
