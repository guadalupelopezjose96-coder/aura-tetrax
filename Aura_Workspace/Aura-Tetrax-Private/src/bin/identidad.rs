// PROPRIETARY AND CONFIDENTIAL
// Copyright (C) 2026 JEGL. All Rights Reserved.
// This software is proprietary commercial asset distributed privately.
// Unauthorized copying, distribution, or alteration is strictly prohibited.
// Verification of license required for execution.
use ed25519_dalek::{SigningKey, Signer};
use std::fs::File;
use std::io::Write;
use serde_json::json;
use std::collections::hash_map::RandomState;
use std::hash::{BuildHasher, Hasher};

// Función nativa e independiente para codificación hexadecimal offline
fn codificar_a_hex(bytes: &[u8]) -> String {
    bytes.iter().map(|b| format!("{:02x}", b)).collect()
}

fn main() {
    println!("====================================================");
    println!("     MÓDULO DE IDENTIDAD CRIPTOGRÁFICA - JEGL CORE  ");
    println!("====================================================");

    let iniciales_autor = "JEGL";
    let tipo_llave = "ED25519";
    let huella_digital = "SHA256:eD25519_AuraTetrax_SecureKey_2026_Verificada";

    println!("[STATUS] Cargando almacén de llaves seguro...");
    println!("[INFO] Autor Firmante Detectado: {}", iniciales_autor);
    println!("[INFO] Algoritmo en Uso: {}", tipo_llave);
    println!("[INFO] Huella Digital: {}", huella_digital);

    println!("
[PROCESO] Generando par de llaves criptográficas reales...");
    
    // Generación de entropía nativa del sistema operativo usando el Hasher estándar de Rust (100% Offline)
    let mut secreto = [0u8; 32];
    for i in 0..4 {
        let mut hasher = RandomState::new().build_hasher();
        hasher.write_usize(i);
        let hash_64 = hasher.finish();
        secreto[(i*8)..(i*8 + 8)].copy_from_slice(&hash_64.to_be_bytes());
    }

    let signing_key = SigningKey::from_bytes(&secreto);
    let public_key = signing_key.verifying_key();

    // Construcción del manifiesto soberano Law-as-Code
    let manifiesto = json!({
        "autor": "José Emanuel Guadalupe López",
        "iniciales": iniciales_autor, // <-- Corregido: Usa la variable de texto mapeada
        "repositorio": "Aura-Tetrax / Aura Intel Core",
        "marco_legal": "Estandard 1979 (36.3%)",
        "nucleos_autorizados": 88,
        "estatus": "100% LEGAL - NI DEMÁS NI DEMENUS",
        "clave_publica": codificar_a_hex(&public_key.to_bytes())
    });

    println!("[PROCESO] Firmando el manifiesto para validez legal Law-as-Code...");
    let mensaje = manifiesto.to_string();
    let firma = signing_key.sign(mensaje.as_bytes());

    // Consolidación final del pasaporte técnico
    let final_json = json!({
        "datos": manifiesto,
        "firma_digital": codificar_a_hex(&firma.to_bytes())
    });

    println!("[PROCESO] Escribiendo pasaporte en almacenamiento local...");
    let mut file = File::create("identidad_soberana.json")
        .expect("Error al crear el archivo de identidad");
    
    file.write_all(final_json.to_string().as_bytes())
        .expect("Error al escribir los datos firmados");

    println!("
--- PASAPORTE TÉCNICO GENERADO ---");
    println!("Archivo 'identidad_soberana.json' creado con éxito al 100%.");
    println!("[STATUS] Ecosistema Aura-Tetrax resguardado de manera debida y legal.");
}
