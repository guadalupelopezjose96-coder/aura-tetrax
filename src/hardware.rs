// SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
// Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
// PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
use sysinfo::{System, SystemExt, CpuExt};

pub fn obtener_hwid_sistema() -> String {
    let mut sys = System::new_all();
    sys.refresh_all();
    
    // Identificador único basado en CPU y nombre de host
    let cpu_info = sys.cpus().get(0).map(|c| c.brand()).unwrap_or("unknown");
    let hostname = sys.host_name().unwrap_or_else(|| "unknown".to_string());
    
    format!("{}-{}", cpu_info.trim(), hostname)
}

