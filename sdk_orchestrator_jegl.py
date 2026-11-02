# SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
# Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
# PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
# sdk_orchestrator_jegl.py
from core.fesm_engine import ejecutar_transaccion_mercado
from database.persistence_layer import guardar_transaccion_db
from core.audit_agent import verificar_integridad_log
from sdk_decryptor_pro_jegl import AuraDecryptor

class SDKOrchestrator:
    """
    Orquestador Central de Aura-Tetrax.
    Punto único de entrada para todas las operaciones del sistema.
    """
    def __init__(self, tesoreria, clave_maestra=None):
        self.tesoreria = tesoreria
        # Capa de seguridad: descifrado de comandos
        self.decriptor = AuraDecryptor(clave_maestra)

    def procesar_comando(self, comando, datos):
        # 1. Seguridad: Desencriptar si el payload es binario
        if isinstance(datos, bytes):
            datos = self.decriptor.descifrar_paquete(datos)
        
        # 2. Dispatcher de protocolos (Lógica de control)
        if comando == "TRANSFERENCIA":
            return self._manejar_transferencia(datos)
        
        elif comando == "AUDITAR":
            return verificar_integridad_log("fesm_audit.log")
        
        elif comando == "STATUS":
            return {"estado": "OK", "saldo": float(self.tesoreria.saldo)}
        
        else:
            return {"estado": "ERROR", "detalle": "Protocolo desconocido"}

    def _manejar_transferencia(self, datos):
        # Ejecución en motor financiero
        resultado = ejecutar_transaccion_mercado(
            datos['emisor'], 
            datos['receptor'], 
            self.tesoreria, 
            datos['monto'], 
            datos['costo'], 
            datos['firma']
        )
        
        # Persistencia atómica (solo si hay éxito)
        if resultado.estado == "EXITO":
            guardar_transaccion_db({
                "emisor": datos['emisor'].id,
                "receptor": datos['receptor'].id,
                "monto": float(datos['monto']),
                "operacion": "TRANSFERENCIA"
            })
            
        return resultado
