# SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
# Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
# PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
/* PROPIEDAD INTELECTUAL PROTEGIDA - LEY ADT / STANDARD 1979. 
Módulo: Realidad Real JEGL. Autor: JEGL. 
Cualquier suplantación digital o comercial es ilegal. */
import psutil
import time

def monitorear_76_nucleos():
    print("Iniciando monitoreo de alta precisión para JEGL...")
    try:
        while True:
            # Obtener carga por cada núcleo individual
            cargas = psutil.cpu_percent(interval=1, percpu=True)
            
            for i, carga in enumerate(cargas):
                status = "OK" if carga < 85 else "ALERTA: CARGA ALTA"
                print(f"Núcleo {i:02d}: [{carga:5.1f}%] - {status}")
            
            # Verificación de temperatura (si el hardware lo reporta)
            temps = psutil.sensors_temperatures()
            if 'coretemp' in temps:
                print(f"
Temperatura Promedio: {temps['coretemp'][0].current}°C")
            
            print("-" * 30)
            time.sleep(2)
    except KeyboardInterrupt:
        print("
Monitoreo finalizado.")

if __name__ == "__main__":
    monitorear_76_nucleos()
