// SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
// Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
// PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
use sha2::{Sha256, Digest};

pub struct ChainManager {
    pub ultimo_hash: String,
}

impl ChainManager {
    pub fn registrar_evento(&mut self, datos: String) -> String {
        let mut hasher = Sha256::new();
        hasher.update(format!("{}{}", self.ultimo_hash, datos));
        let nuevo_hash = format!("{:x}", hasher.finalize());
        self.ultimo_hash = nuevo_hash.clone();
        nuevo_hash
    }
}
