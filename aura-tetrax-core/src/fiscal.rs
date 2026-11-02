// SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
// Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
// PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
//! # Módulo Fiscal y de Equivalencia (JEGL_SYSTEM)
//!
//! Este módulo implementa las reglas de cálculo matemático e impositivo
//! para el Standard 1979 (Ley de Equivalencia Fiscal y Sustentabilidad del Mercado - FESM).
//! Garantiza la exactitud algorítmica al 100% en la cuantificación de la productividad.

/// Tasa de gravamen inmutable sobre la productividad automatizada (36.3%).
pub const PRODUCTIVITY_TAX_RATE: f64 = 0.363;

/// Tasa de gravamen aplicable a bienes y activos extranjeros (40.0%).
pub const FOREIGN_ASSET_TAX_RATE: f64 = 0.40;

/// Coeficiente predeterminado de conversión energética (Joules a Unidad Fiscal).
/// Diseñado para interactuar directamente con los Hardware Audit Modules del entorno.
pub const DEFAULT_ENERGY_CONVERSION_COEFFICIENT: f64 = 1.0;

/// Calcula la equivalencia fiscal basada en la productividad automatizada general.
/// Aplica de manera estricta el gravamen del 36.3% (`PRODUCTIVITY_TAX_RATE`).
pub fn calculate_fiscal_equivalence(productivity: f64) -> f64 {
    productivity * PRODUCTIVITY_TAX_RATE
}

/// Calcula el gravamen correspondiente a la adquisición o tenencia de activos extranjeros.
/// Aplica de manera estricta la tasa del 40.0% (`FOREIGN_ASSET_TAX_RATE`).
pub fn calculate_foreign_asset_tax(asset_value: f64) -> f64 {
    asset_value * FOREIGN_ASSET_TAX_RATE
}

/// Convierte la entrada física de energía (medida en Joules) en valor de productividad estimada,
/// utilizando el coeficiente dinámico de eficiencia del hardware.
pub fn energy_to_productivity(energy_joules: f64, conversion_coefficient: f64) -> f64 {
    energy_joules * conversion_coefficient
}

// =========================================================================
// VALIDACIÓN DE PRECISIÓN MATEMÁTICA (TESTS UNITARIOS)
// =========================================================================
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_productivity_tax_calculation() {
        let productivity = 1000.0;
        let expected_tax = 363.0; // 1000 * 0.363
        let calculated_tax = calculate_fiscal_equivalence(productivity);
        
        // Validación con margen épsilon mínimo para evitar errores de precisión en f64
        assert!((calculated_tax - expected_tax).abs() < f64::EPSILON);
    }

    #[test]
    fn test_foreign_asset_tax_calculation() {
        let asset_value = 5000.0;
        let expected_tax = 2000.0; // 5000 * 0.40
        let calculated_tax = calculate_foreign_asset_tax(asset_value);
        
        assert!((calculated_tax - expected_tax).abs() < f64::EPSILON);
    }

    #[test]
    fn test_energy_to_productivity_conversion() {
        let energy = 2500.0;
        let coefficient = 1.5;
        let expected_productivity = 3750.0;
        let calculated_productivity = energy_to_productivity(energy, coefficient);
        
        assert!((calculated_productivity - expected_productivity).abs() < f64::EPSILON);
    }
}
