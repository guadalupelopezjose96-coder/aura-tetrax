#!/usr/bin/env python3
import os

# CONFIGURACIÓN: Ajusta estos valores conforme realices tus pagos
DEUDA_INICIAL = {"Google_Workspace": 1273.57, "Cloudflare": 60.50}
PAGOS_REALIZADOS = {"Google_Workspace": 0.00, "Cloudflare": 0.00}

FILE_PATH = os.path.expanduser("~/bitacora_fiscal.txt")

def actualizar_auditoria():
    with open(FILE_PATH, "w") as f:
        f.write("--- BITÁCORA FISCAL SOBERANA: PLAN DE LIQUIDACIÓN ---\n")
        total_restante = 0
        
        for servicio in DEUDA_INICIAL:
            restante = DEUDA_INICIAL[servicio] - PAGOS_REALIZADOS[servicio]
            total_restante += restante
            f.write(f"Servicio: {servicio}\n")
            f.write(f"  - Pendiente original: ${DEUDA_INICIAL[servicio]:.2f}\n")
            f.write(f"  - Pagado hasta hoy:   ${PAGOS_REALIZADOS[servicio]:.2f}\n")
            f.write(f"  - Saldo actual:       ${restante:.2f}\n\n")
            
        f.write(f"TOTAL ADEUDADO A LIQUIDAR: ${total_restante:.2f}\n")
        f.write("Estado: 100% REGISTRADO Y AUDITABLE\n")

if __name__ == "__main__":
    actualizar_auditoria()
    print("Plan de liquidación actualizado al 100% en ~/bitacora_fiscal.txt")
