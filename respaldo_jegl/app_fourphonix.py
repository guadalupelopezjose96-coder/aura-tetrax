# SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
# Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
# PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

import os
import subprocess
import time
from flask import Flask, render_template, request, send_from_directory, abort
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Rutas de Soberanía al 100%
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
RESULT_FOLDER = os.path.join(BASE_DIR, 'AURA_SANADOS')
ENGINE_PATH = os.path.join(BASE_DIR, 'target/release/aura_intel_core')

# Garantizar Infraestructura
for folder in [UPLOAD_FOLDER, RESULT_FOLDER]:
    os.makedirs(folder, exist_ok=True)

def audit_log(msg):
    with open("AURA_FINANCE_AUDIT.log", "a") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {msg}\n")

@app.route('/')
def lobby():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def process_media():
    if 'file' not in request.files: return abort(400)
    file = request.files['file']
    if file.filename == '': return abort(400)

    fname = secure_filename(file.filename)
    in_p = os.path.join(UPLOAD_FOLDER, fname)
    out_n = f"SANADO_{fname}"
    out_p = os.path.join(RESULT_FOLDER, out_n)

    file.save(in_p)
    audit_log(f"INICIO: {fname}")

    # COMANDO MAESTRO: Conexión FFmpeg -> Rust Engine -> FFmpeg Output
    # Tasa 36.3% aplicada en tiempo de ejecución
    cmd = (
        f"ffmpeg -y -i {in_p} -f rawvideo -pix_fmt rgba - | "
        f"{ENGINE_PATH} | "
        f"ffmpeg -y -f rawvideo -pixel_format rgba -video_size 1920x1080 -i - "
        f"-c:v libx264 -preset ultrafast -pix_fmt yuv420p {out_p}"
    )

    try:
        start = time.time()
        subprocess.run(cmd, shell=True, check=True)
        dur = time.time() - start
        audit_log(f"FIN: {out_n} en {dur:.2f}s")

        return f"""
        <body style="background:#000;color:#d4af37;text-align:center;padding-top:100px;font-family:monospace;">
            <h1>✅ SANEAMIENTO COMPLETADO</h1>
            <p>Tiempos de procesamiento: {dur:.2f}s</p>
            <a href="/download/{out_n}" style="color:#fff;border:1px solid #d4af37;padding:10px;text-decoration:none;">DESCARGAR ACTIVO ÉLITE</a>
            <br><br><a href="/" style="color:#555;">Volver</a>
        </body>
        """
    except Exception as e:
        audit_log(f"ERROR: {str(e)}")
        return f"Error en el Core: {str(e)}", 500

@app.route('/download/<filename>')
def serve_result(filename):
    return send_from_directory(RESULT_FOLDER, filename)

if __name__ == "__main__":
    # Puerto Phi 1618 para Soberanía de Red
    app.run(host='0.0.0.0', port=1618)
