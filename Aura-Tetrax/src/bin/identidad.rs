// PROPRIETARY AND CONFIDENTIAL
// Copyright (C) 2026 JEGL. All Rights Reserved.
// This software is proprietary commercial asset distributed privately.
// Unauthorized copying, distribution, or alteration is strictly prohibited.
// Verification of license required for execution.
// src/bin/identidad.rs
use ed25519_dalek::{SigningKey, Signer};
use rand::rngs::OsRng;
use std::fs::File;
use std::io::Write;
use serde_json::json;

fn main() {
    let _csprng = OsRng;
    let signing_key = SigningKey::generate(&mut OsRng);
    let public_key = signing_key.verifying_key();

    let manifiesto = json!({
        "autor": "José Emanuel Guadalupe López",
        "iniciales": "JEGL",
        "proyecto": "Aura-Tetrax / Aura Intel Core",
        "ley": "Estándar 1979 (36.3%)",
        "nucleos_autorizados": 88,
        "estatus": "100% LEGAL - NI DEMÁS NI DEMENUS",
        "clave_publica": hex::encode(public_key.to_bytes())
    });

    // Firmar el manifiesto para validez legal Law-as-Code
    let mensaje = manifiesto.to_string();
    let firma = signing_key.sign(mensaje.as_bytes());

    let final_json = json!({
        "datos": manifiesto,
        "firma_digital": hex::encode(firma.to_bytes())
    });

    let mut file = File::create("identidad_soberana.json").expect("Error al crear archivo");
    file.write_all(final_json.to_string().as_bytes()).expect("Error al escribir");

    println!("--- PASAPORTE TÉCNICO GENERADO ---");
    println!("Archivo 'identidad_soberana.json' creado con éxito al 100%.");
}
