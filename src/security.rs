// src/security.rs
// Módulo de Seguridad y Soberanía Digital para Tetrax Engine Pro
// Autor: JEGL (José Emanuel Guadalupe López)

use ed25519_dalek::{Verifier, Signature, PublicKey};

/// Llave pública ED25519 embebida en la sección .rodata (Read-Only)
/// NOTA: Reemplaza estos 32 bytes con los valores hexadecimales reales de tu llave pública.
pub const PUBLIC_KEY_BYTES: [u8; 32] = [
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
];

/// Verifica la integridad del binario o activo contra una firma digital.
/// Esta función es determinista, inline y no realiza asignaciones en el heap.
#[inline(always)]
pub fn verify_signature(data: &[u8], signature_bytes: &[u8]) -> bool {
    // Conversión segura de la llave pública
    let public_key = match PublicKey::from_bytes(&PUBLIC_KEY_BYTES) {
        Ok(pk) => pk,
        Err(_) => return false,
    };

    // Conversión segura de la firma recibida
    let signature = match Signature::from_bytes(signature_bytes) {
        Ok(sig) => sig,
        Err(_) => return false,
    };

    // Verificación criptográfica ED25519
    public_key.verify(data, &signature).is_ok()
}

/// Mecanismo Fail-safe para el cumplimiento del Manual FESM.
/// Detiene la ejecución instantáneamente ante cualquier intento de manipulación.
pub fn trigger_security_shutdown() {
    eprintln!("ALERTA DE SEGURIDAD: Violación de integridad detectada en Tetrax Engine Pro.");
    // Exit code 1 para indicar fallo de seguridad según Standard 1979
    std::process::exit(1);
}

/// Muestra el aviso legal de propiedad privada al iniciar el motor.
pub fn display_disclaimer() {
    println!("Tetrax Engine Pro - Activo Propietario JEGL.");
    println!("Uso sujeto a contrato privado y Standard 1979 (FESM).");
}
