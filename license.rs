// SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
// Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
// PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))

use std::time::{SystemTime, UNIX_EPOCH};

// Estructura que representa el Token de Licencia vinculado al hardware/usuario
struct LicenseToken {
    token_id: String,
    activation_timestamp: u64, // Epoch time de activación
    validity_duration: u64,    // 365 días en segundos (31,536,000)
}

impl LicenseToken {
    fn is_valid(&self) -> bool {
        let now = SystemTime::now()
            .duration_since(UNIX_EPOCH)
            .expect("Error al obtener tiempo del sistema")
            .as_secs();

        // Verifica si estamos dentro del margen de 365 días
        now < (self.activation_timestamp + self.validity_duration)
    }

    fn check_hard_lock(&self) {
        if !self.is_valid() {
            // Hard-Lock: El motor de geometría sónica se detiene
            println!("ERROR [JEGL-ADT]: Licencia expirada. Contacte con el administrador para renovación.");
            std::process::exit(1);
        } else {
            println!("Sistema autorizado: Aura-Tetrax Pro activo.");
        }
    }
}

fn main() {
    // Ejemplo de un token activado
    let user_token = LicenseToken {
        token_id: String::from("ED25519-JEGL-2026-05-20"),
        activation_timestamp: 1779434125, // Fecha base de activación
        validity_duration: 31536000,
    };

    user_token.check_hard_lock();
}
