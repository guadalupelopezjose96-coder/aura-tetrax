# SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
# Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
# PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
# cli_interface.py
import sys
from decimal import Decimal
from sdk_orchestrator_jegl import SDKOrchestrator
from core.fesm_engine import TransaccionResultado
from test_full_integration import Entidad, cargar_clave_privada, firmar_transaccion

def iniciar_interfaz():
    # 1. Inicialización del Sistema
    tesoreria = Entidad("TES_001", "0.00")
    orquestador = SDKOrchestrator(tesoreria)
    
    # Cargar identidad del emisor para la sesión
    try:
        emisor = Entidad("USR_001", "1000.00", clave_privada=cargar_clave_privada("emisor"))
        emisor.clave_publica = emisor.clave_privada.public_key()
    except Exception as e:
        print(f"Error de seguridad: No se pudieron cargar las llaves. {e}")
        return

    receptor = Entidad("USR_002", "500.00")

    print("\n--- Aura-Tetrax Financial CLI v1.0 ---")
    
    while True:
        print("\nOpciones: [1] Transferencia [2] Auditar Estado [3] Salir")
        opcion = input("Seleccione comando: ")
        
        if opcion == "1":
            # Ejecución de transferencia blindada
            try:
                monto = Decimal(input("Ingrese monto a transferir: "))
                mensaje = f"{emisor.id}:{receptor.id}:{monto}".encode()
                firma = firmar_transaccion(emisor.clave_privada, mensaje)
                
                datos = {
                    'emisor': emisor, 'receptor': receptor,
                    'monto': monto, 'costo': Decimal('1.00'), 'firma': firma
                }
                
                resultado = orquestador.procesar_comando("TRANSFERENCIA", datos)
                print(f"\n[ESTADO]: {resultado.estado}")
                print(f"[DETALLE]: {resultado.detalle}")
            except Exception as e:
                print(f"Error en transacción: {e}")

        elif opcion == "2":
            # Ejecución de auditoría de integridad
            reporte = orquestador.procesar_comando("AUDITAR", {})
            print(f"\n--- Reporte de Integridad ---")
            print(f"Estado de Salud: {reporte.get('estado_salud')}")
            print(f"Alertas detectadas: {reporte.get('alertas')}")
            print(f"Total auditable: {reporte.get('total_transacciones')}")
            
        elif opcion == "3":
            print("Cerrando sesión de Aura-Tetrax...")
            break
        else:
            print("Comando no reconocido.")

if __name__ == "__main__":
    iniciar_interfaz()
