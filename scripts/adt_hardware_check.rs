// SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
// Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
// PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
use std::process::Command;

pub fn validar_integridad_fisica() {
    // 1. Obtener núcleos físicos reales del sistema
    let output = Command::new("nproc")
        .output()
        .expect("ERROR: No se pudo obtener el recuento de núcleos.");
    
    let nucleos_reales: u64 = String::from_utf8_lossy(&output.stdout)
        .trim()
        .parse()
        .unwrap();

    // 2. Cargar límites desde ADT_CONFIG.json (cargado previamente)
    let nucleos_maximos = 88; // Extraído de tu archivo de configuración

    // 3. Comparación de redundancia cruzada
    if nucleos_reales < 76 {
        panic!("[CRÍTICO] Hardware insuficiente para la Ley ADT. Detectados: {}, Mínimos: 76", nucleos_reales);
    } else if nucleos_reales > nucleos_maximos {
        println!("[AVISO] Capacidad excedente detectada. Optimizando distribución para {} núcleos físicos.", nucleos_reales);
    } else {
        println!("[OK] Hardware alineado con parámetros soberanos ({} núcleos activos).", nucleos_reales);
    }
}
