// SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
// Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
// PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
// src/licensing.rs
use sha2::{Sha256, Digest};
use std::process::Command;

/// Función para obtener el hash del serial del hardware.
/// Esto asegura que el ID real nunca sea legible en el binario.
pub fn get_hardware_id_hash() -> String {
    let output = Command::new("getprop")
        .arg("ro.serialno")
        .output()
        .expect("Error al obtener ID");
    
    let serial = String::from_utf8_lossy(&output.stdout).trim();
    
    // Calcular SHA-256 del serial
    let mut hasher = Sha256::new();
    hasher.update(serial.as_bytes());
    let result = hasher.finalize();
    
    format!("{:x}", result) // Retorna el hash en formato hexadecimal
}

/// Validación contra lista de hashes autorizados
pub fn is_device_authorized(hw_hash: &str) -> bool {
    // Lista de hashes de los dispositivos permitidos (ejemplo)
    // Estos hashes fueron generados previamente a partir de los seriales reales
    let authorized_hashes = vec![
        "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", // Hash de muestra
        "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
    ];
    
    authorized_hashes.contains(&hw_hash.to_string())
}

pub fn check_license() -> bool {
    let hw_hash = get_hardware_id_hash();
    if is_device_authorized(&hw_hash) {
        true
    } else {
        // Log de auditoría para el Manual de Cumplimiento FESM
        eprintln!("ACCESO DENEGADO: Hardware ID Hash no reconocido: {}", hw_hash);
        false
    }
}
