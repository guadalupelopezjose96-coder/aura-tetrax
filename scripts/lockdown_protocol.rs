// SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
// Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
// PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
use std::process::Command;

pub fn activar_lockdown() {
    println!("[!] ALERTA: INTENTO DE ACCESO NO AUTORIZADO DETECTADO.");
    println!("[!] Iniciando protocolo de Lockdown...");

    // Revocar permisos de escritura y lectura de los scripts críticos
    Command::new("chmod")
        .args(["-R", "000", "/home/user/scripts/"])
        .status()
        .expect("Error al ejecutar Lockdown.");

    // Registrar en FESM
    Command::new("logger")
        .arg("CRÍTICO: Acceso no autorizado. Sistema en modo Lockdown.")
        .status()
        .ok();
}
