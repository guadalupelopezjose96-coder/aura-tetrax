// PROPRIETARY AND CONFIDENTIAL
// Copyright (C) 2026 JEGL. All Rights Reserved.
// This software is proprietary commercial asset distributed privately.
// Unauthorized copying, distribution, or alteration is strictly prohibited.
// Verification of license required for execution.
// Frecuencias base del sistema de sincronización digital
pub const FREQ_NATURAL: f64 = 432.0;
pub const FREQ_REGENERATIVA: f64 = 528.0;
pub const SAMPLE_RATE: usize = 48000;

pub struct SonicEngine {
    lookup_432: Vec<f32>,
    lookup_528: Vec<f32>,
}

impl SonicEngine {
    // Inicializa las tablas de consulta para ejecución instantánea
    pub fn new() -> Self {
        let mut lookup_432 = vec![0.0; SAMPLE_RATE];
        let mut lookup_528 = vec![0.0; SAMPLE_RATE];
        
        for i in 0..SAMPLE_RATE {
            let t = i as f64 / SAMPLE_RATE as f64;
            lookup_432[i] = (2.0 * std::f64::consts::PI * FREQ_NATURAL * t).sin() as f32;
            lookup_528[i] = (2.0 * std::f64::consts::PI * FREQ_REGENERATIVA * t).sin() as f32;
        }
        
        SonicEngine { lookup_432, lookup_528 }
    }

    // Ejecución paralela masiva libre de bloqueos
    pub fn procesar_matriz_paralela(&self, buffer: &mut [f32], usar_528: bool) {
        use rayon::prelude::*;
        
        // Divide el procesamiento entre los núcleos lógicos disponibles de forma síncrona
        buffer.par_iter_mut().enumerate().for_each(|(idx, sample)| {
            let lookup_idx = idx % SAMPLE_RATE;
            *sample = if usar_528 {
                self.lookup_528[lookup_idx]
            } else {
                self.lookup_432[lookup_idx]
            };
        });
    }
}
