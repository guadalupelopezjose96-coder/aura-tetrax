// SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
// Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
// PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
use std::process::Command;

pub fn firmar_log_telemetria(nombre_archivo: &str) -> Result<(), String> {
    let estatus = Command::new("gpg")
        .args(["--batch", "--yes", "--detach-sign", "--armor", nombre_archivo])
        .status()
        .map_err(|e| e.to_string())?;

    if estatus.success() { Ok(()) } else { Err("Error en firma GPG".to_string()) }
}
