// SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
// Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
// PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
use std::process::Command;

pub fn replicar_estado_soberano(nodo_destino: &str) {
    println!("[SYNC] Iniciando réplica inmutable hacia: {}", nodo_destino);
    
    // El respaldo se realiza mediante rsync con cifrado SSH
    let status = Command::new("rsync")
        .args(["-avz", "--checksum", "./scripts/", format!("user@{}:/home/user/scripts/", nodo_destino)])
        .status()
        .expect("ERROR: Fallo en la sincronización de soberanía.");

    if status.success() {
        println!("[OK] Nodo {} sincronizado. Soberanía replicada.", nodo_destino);
    }
}
