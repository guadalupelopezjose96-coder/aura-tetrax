// SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
// Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
// PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
use std::time::{SystemTime, UNIX_EPOCH};
use sha2::{Sha256, Digest};

pub struct TelemetriaAuditiva {
    pub frecuencia: f64,
    pub timestamp: u128,
    pub estado_legal: String,
}

impl TelemetriaAuditiva {
    pub fn validar_frecuencia(&self) -> bool {
        let error_maximo = 0.01;
        (self.frecuencia - 432.0).abs() < error_maximo || (self.frecuencia - 528.0).abs() < error_maximo
    }

    pub fn generar_hash(&self) -> String {
        let mut hasher = Sha256::new();
        hasher.update(format!("{}{}{}", self.frecuencia, self.timestamp, self.estado_legal));
        format!("{:x}", hasher.finalize())
    }
}
