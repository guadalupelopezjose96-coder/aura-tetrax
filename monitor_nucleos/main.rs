// SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
// Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
// PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
use std::process::Command;

fn verificar_y_cargar_config() -> Result<String, String> {
    let home = std::env::var("HOME").unwrap();
    let config = format!("{}/aura_tetrax_pro/config/adt_params.json", home);
    let signature = format!("{}.asc", config);

    // Ejecuta gpg --verify para asegurar la integridad
    let status = Command::new("gpg")
        .args(["--verify", &signature, &config])
        .status()
        .map_err(|e| format!("Error al ejecutar gpg: {}", e))?;

    if status.success() {
        println!("Firma verificada: Ley ADT aplicada correctamente.");
        Ok(std::fs::read_to_string(config).unwrap())
    } else {
        Err("ALERTA DE SEGURIDAD: La firma es inválida. El sistema se detendrá.".to_string())
    }
}

