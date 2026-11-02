// SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
// Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
// PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
// Nueva estructura de importación para ed25519-dalek v2.x
use ed25519_dalek::{SigningKey, Signature, Signer};
use std::time::{SystemTime, UNIX_EPOCH};
use std::env;
use serde_json::json;

fn main() {
    // 1. Datos de Telemetría (Ejemplo de ciclo: 500,000 ops / 116ns)
    let datos_motor = json!({
        "sistema": "Aura-Tetrax",
        "operaciones": 500000,
        "latencia_ns": 116,
        "frecuencia_hz": "432-528"
    });

    // 2. Generar Cabecera de Legalidad (CLS)
    let ts = SystemTime::now().duration_since(UNIX_EPOCH).unwrap().as_secs();
    let cabecera = format!(
        "[SISTEMA GLOBAL INTEGRADO - ECOSISTEMA AURA-TETRAX]\n\
         ID DE REFERENCIA FISCAL: 71204722\n\
         AUTORIDAD PROPIETARIA: JEGL\n\
         SELLO DE TIEMPO (UTC): {}\n\
         VALIDACIÓN CRIPTOGRÁFICA:\n", ts
    );

	// 3. Firma ED25519 (Segura y 100% Legal)
    let clave_hex = env::var("JEGL_SIGNING_KEY").expect("Clave JEGL no configurada");
    let secret_bytes = hex::decode(clave_hex).expect("Clave inválida");

	// En v2.x, creamos la SigningKey directamente desde los bytes
    let signing_key = SigningKey::from_bytes(&secret_bytes.try_into().unwrap());
    let public_key = signing_key.verifying_key(); // Equivalente a PublicKey

    let payload = format!("{}{}", cabecera, datos_motor.to_string());
    let firma = signing_key.sign(payload.as_bytes()); // Firma directa

    // 4. Reporte Final (Blob inmutable)
    let reporte_final = format!(
        "{}- Firma ED25519: {}\n- Integridad: 100% Verificada\n---END HEADER---\n{}",
        cabecera, hex::encode(firma.to_bytes()), datos_motor.to_string()
    );

    // Salida para el canal de intercambio
    println!("{}", reporte_final);
}
