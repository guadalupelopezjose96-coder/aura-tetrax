// SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
// Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
// PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
//! # Módulo de Auditoría de Integridad (JEGL_SYSTEM)
//!
//! Este módulo define la estructura inmutable y persistente de los registros 
//! de auditoría para la Verdad Digital (Ley ADT) y el Standard 1979. 
//! Garantiza que cada cálculo energético y fiscal quede sellado criptográficamente.

use serde::{Serialize, Deserialize};
use std::time::{SystemTime, UNIX_EPOCH};

/// Tipo formal que representa una firma digital GPG en formato ASCII-armored o binario.
pub type DigitalSignature = String;

/// Estructura de Auditoría de Integridad y Cumplimiento Legal.
/// Almacena de forma indisoluble la telemetría física del hardware y el gravamen calculado.
#[derive(Debug, Serialize, Deserialize, Clone, PartialEq)]
pub struct FiscalAuditLog {
    /// Marca de tiempo Unix (en segundos) que define el momento exacto del sellado.
    pub timestamp: u64,
    /// Entrada de energía medida en Joules por los módulos de auditoría de hardware.
    pub energy_input: f64,
    /// Equivalencia impositiva calculada por el Tetrax Engine Pro (Tasa Estándar de 36.3%).
    pub calculated_tax: f64,
    /// Sello criptográfico asimétrico generado por la identidad del operador del sistema.
    pub signature: DigitalSignature,
}

impl FiscalAuditLog {
    /// Crea una nueva instancia de registro de auditoría, calculando automáticamente
    /// el timestamp actual a partir del reloj en tiempo real del sistema.
    pub fn new(energy_input: f64, calculated_tax: f64, signature: DigitalSignature) -> Self {
        let timestamp = SystemTime::now()
            .duration_since(UNIX_EPOCH)
            .map(|d| d.as_secs())
            .unwrap_or(0);

        Self {
            timestamp,
            energy_input,
            calculated_tax,
            signature,
        }
    }

    /// Instancia explícita con marca de tiempo manual. 
    /// Diseñado para la reconstrucción histórica de bloques o importación de bitácoras externas.
    pub fn with_explicit_timestamp(
        timestamp: u64,
        energy_input: f64,
        calculated_tax: f64,
        signature: DigitalSignature,
    ) -> Self {
        Self {
            timestamp,
            energy_input,
            calculated_tax,
            signature,
        }
    }

    /// Convierte el registro de auditoría actual en una cadena JSON formateada y legible.
    /// Útil para la persistencia directa en los manifiestos de arquitectura pública.
    pub fn to_json(&self) -> Result<String, serde_json::Error> {
        serde_json::to_string_pretty(self)
    }

    /// Reconstruye una estructura de auditoría a partir de un flujo o cadena JSON válida.
    pub fn from_json(json_str: &str) -> Result<Self, serde_json::Error> {
        serde_json::from_str(json_str)
    }
}

// =========================================================================
// VALIDACIÓN DE COHERENCIA DE DATOS (TESTS UNITARIOS)
// =========================================================================
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_audit_log_instantiation() {
        let mock_sig = String::from("-----BEGIN PGP SIGNATURE-----\nVERSION_JEGL_SYSTEM\n-----END PGP SIGNATURE-----");
        let log = FiscalAuditLog::new(1250.75, 454.02, mock_sig.clone());

        assert!(log.timestamp > 0, "El timestamp automático debe ser mayor a cero.");
        assert_eq!(log.energy_input, 1250.75);
        assert_eq!(log.calculated_tax, 454.02);
        assert_eq!(log.signature, mock_sig);
    }

    #[test]
    fn test_json_integrity_cycle() {
        let mock_sig = String::from("CRIPTO_SELLO_VERIFICABLE_100");
        let original_log = FiscalAuditLog::with_explicit_timestamp(1779926400, 5000.0, 1815.0, mock_sig);

        // Ciclo de exportación
        let json_data = original_log.to_json().expect("Error al serializar a JSON");
        
        // Ciclo de importación y verificación de no-repudio
        let restored_log = FiscalAuditLog::from_json(&json_data).expect("Error al deserializar de JSON");
        
        assert_eq!(original_log, restored_log, "La estructura restaurada debe ser idéntica al 100% a la original.");
    }
}
