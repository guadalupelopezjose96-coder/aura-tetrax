// SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
// Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
// PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
pub struct Activo {
    pub valor: f64,
}

impl Activo {
    pub fn nuevo(valor_input: f64) -> Result<Self, String> {
        // Ejecución de la Ley Irrevocable: El 100% de lo que sea <= 0 es ilegal.
        if valor_input <= 0.0 {
            // Acción: Revocación total de la operación
            return Err("ERROR CRÍTICO: Violación de Ley Irrevocable. Valor nulo o negativo detectado en Activo.".to_string());
        }
        
        Ok(Activo { valor: valor_input })
    }

    pub fn procesar_valor(&self) -> f64 {
        // Garantía de integridad constante
        assert!(self.valor > 0.0, "VIOLACIÓN DE LEY: Se ha detectado un valor no-positivo en el sistema.");
        self.valor
    }
}
