// SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
// Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
// PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
//! # Punto de Entrada Ejecutable - Aura-Tetrax Core (JEGL_SYSTEM)
//!
//! Convierte el núcleo en un binario ejecutable capaz de simular la captura
//! de telemetría, procesar la equivalencia fiscal del Standard 1979
//! y emitir el manifiesto JSON estructurado con el sello lógico.

use aura_tetrax_core::{
    audit::FiscalAuditLog,
    fiscal::{calculate_fiscal_equivalence, energy_to_productivity, DEFAULT_ENERGY_CONVERSION_COEFFICIENT},
    verify_core_status, OPERATOR_NAME, GOVERNANCE_STANDARD
};

fn main() {
    println!("=========================================================================");
    println!(" INICIALIZANDO ENTORNO: {} ", OPERATOR_NAME);
    println!(" NÚCLEO DE GOBERNANZA:  {} ", GOVERNANCE_STANDARD);
    println!("=========================================================================");
    
    // 1. Verificar el estado del núcleo básico de forma inmediata
    let status = verify_core_status();
    println!("[+] Estado: {}", status);

    // 2. Simulación de captura de telemetría de hardware (Capa de Eficiencia Energética)
    // Carga de trabajo base estimada para entornos de alto rendimiento.
    let simulated_energy_joules = 12500.0; 
    println!("[+] Telemetría Física: {:.2} Joules detectados en la capa de hardware.", simulated_energy_joules);

    // 3. Procesar conversión de energía a productividad bruta
    let productivity = energy_to_productivity(simulated_energy_joules, DEFAULT_ENERGY_CONVERSION_COEFFICIENT);
    
    // 4. Calcular la equivalencia fiscal del Standard 1979 (Tasa Estándar del 36.3%)
    let tax = calculate_fiscal_equivalence(productivity);
    println!("[+] Tetrax Engine Pro: Equivalencia impositiva calculada: {:.4}", tax);

    // 5. Estructurar el Sello Criptográfico Ley ADT
    // Nota: En la automatización final del despliegue, esta firma se extrae 
    // directamente a través del script de validación externa `.sh` con tu llave GPG.
    let mock_gpg_signature = format!(
        "-----BEGIN PGP SIGNATURE-----\nVersion: GnuPG v2\nOperator: {}\nHash: SHA256\n[SELLO_CRIPTOGRAFICO_VALIDADO_100]\n-----END PGP SIGNATURE-----",
        OPERATOR_NAME
    );

    // 6. Instanciar y consolidar el Registro de Auditoría Inmutable
    let audit_log = FiscalAuditLog::new(simulated_energy_joules, tax, mock_gpg_signature);

    // 7. Exportar el manifiesto resultante a formato JSON legible para el registro público
    match audit_log.to_json() {
        Ok(json_manifest) => {
            println!("\n[JEGL_SYSTEM] >>> MANIFIESTO DE AUDITORÍA GENERADO EXITOSAMENTE <<<");
            println!("{}", json_manifest);
        }
        Err(e) => {
            eprintln!("[-] Error crítico al serializar el manifiesto JSON: {}", e);
        }
    }
    println!("=========================================================================");
}
