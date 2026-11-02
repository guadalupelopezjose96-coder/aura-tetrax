#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
# Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
# PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
import os
import json
import sys
import logging
from datetime import datetime
import google.generativeai as genai

# --- Configuración de rutas (Estructura Aura-Tetrax) ---
CONFIG_PATH = os.path.expanduser('~/Aura-Tetrax/config/aura-config.json')
AUDIT_LOG_PATH = os.path.expanduser('~/Aura-Tetrax/audit/gemini_bridge.log')

# --- Configuración de Logging para Auditoría ADT ---
logging.basicConfig(
    filename=AUDIT_LOG_PATH,
    level=logging.INFO,
    format='%(asctime)s - [AUDIT] - %(message)s'
)

def load_config():
    """Carga la configuración con validación 100% soberana."""
    if not os.path.exists(CONFIG_PATH):
        print("ERROR: Archivo de configuración no encontrado.")
        sys.exit(1)
    
    with open(CONFIG_PATH, 'r') as f:
        return json.load(f)

def get_gemini_response(prompt):
    """Interfaz segura hacia la API de Gemini."""
    try:
        config = load_config()
        api_key = config.get('gemini_api_key')
        
        if not api_key:
            return "ERROR: API Key no configurada en aura-config.json."

        # Configuración del modelo
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Generación de contenido
        response = model.generate_content(prompt)
        
        # Auditoría del evento
        logging.info(f"PROMPT: {prompt} | STATUS: SUCCESS")
        
        return response.text

    except Exception as e:
        logging.error(f"PROMPT: {prompt} | ERROR: {str(e)}")
        return f"ERROR de Sistema: {str(e)}"

if __name__ == "__main__":
    # Captura de input desde la terminal o argumentos
    if len(sys.argv) > 1:
        user_prompt = " ".join(sys.argv[1:])
        result = get_gemini_response(user_prompt)
        print(result)
    else:
        print("Uso: python3 gemini_bridge.py 'Tu consulta aquí'")
