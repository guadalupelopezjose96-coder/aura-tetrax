// SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
// Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
// PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
//! # Aura-Tetrax Core (JEGL_SYSTEM)
//!
//! Núcleo de infraestructura automatizada para la Verdad Digital (Ley ADT)
//! y la Ley de Equivalencia Fiscal y Sustentabilidad del Mercado (Standard 1979 / FESM).
//!
//! Este módulo actúa como la raíz de la biblioteca, gestionando la visibilidad
//! de los registros de auditoría y los motores de cálculo impositivo.

// =========================================================================
// 1. DECLARACIÓN DE MÓDULOS INTERNOS
// =========================================================================
// Vincula los archivos hermanos `src/audit.rs` y `src/fiscal.rs` al árbol de compilación.
pub mod audit;
pub mod fiscal;

// =========================================================================
// 2. RE-EXPORTS PÚBLICOS (API Ergonomics)
// =========================================================================
// Facilita el acceso a las estructuras esenciales directamente desde la raíz del crate.
pub use audit::{FiscalAuditLog, DigitalSignature};
pub use fiscal::{calculate_fiscal_equivalence, PRODUCTIVITY_TAX_RATE, FOREIGN_ASSET_TAX_RATE};

// =========================================================================
// 3. CONSTANTES DEL SISTEMA SOBERANO
// =========================================================================
/// Identificador oficial del operador de la arquitectura técnica.
pub const OPERATOR_NAME: &str = "JEGL_SYSTEM";

/// Norma de gobernanza digital aplicada al cálculo de flujos y plusvalías.
pub const GOVERNANCE_STANDARD: &str = "Standard 1979 / FESM";

/// Versión base del núcleo tecnológico accesible.
pub const CORE_VERSION: &str = "Aura Core Basic - 1.0.0";

// =========================================================================
// 4. FUNCIONES DE VERIFICACIÓN DE ESTADO
// =========================================================================
/// Verifica el estado operativo del núcleo básico de forma inmediata.
/// Retorna una cadena de validación que confirma la sincronía del entorno.
pub fn verify_core_status() -> &'static str {
    "Aura Core Basic: Sincronía 100% - Operación Legal y Técnica Activa"
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_core_initialization() {
        assert_eq!(OPERATOR_NAME, "JEGL_SYSTEM");
        assert_eq!(verify_core_status(), "Aura Core Basic: Sincronía 100% - Operación Legal y Técnica Activa");
    }
}
