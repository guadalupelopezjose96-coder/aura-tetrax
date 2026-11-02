// SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
// Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
// PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
use reqwest::blocking::Client;
use serde::{Deserialize, Serialize};

#[derive(Serialize)]
struct AuthPayload { hwid: String, license_key: String }

#[derive(Deserialize)]
struct AuthResponse { status: String, token: Option<String> }

pub fn validar_acceso(hwid: &str, key: &str) -> bool {
    let client = Client::new();
    let payload = AuthPayload { hwid: hwid.to_string(), license_key: key.to_string() };

    let res = client.post("https://tudominio.com/validar")
        .json(&payload)
        .send();

    match res {
        Ok(r) => {
            let auth: AuthResponse = r.json().unwrap_or(AuthResponse { status: "DENIED".to_string(), token: None });
            auth.status == "OK"
        },
        Err(_) => false,
    }
}
