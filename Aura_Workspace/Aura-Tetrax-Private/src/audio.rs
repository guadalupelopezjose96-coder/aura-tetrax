// PROPRIETARY AND CONFIDENTIAL
// Copyright (C) 2026 JEGL. All Rights Reserved.
// This software is proprietary commercial asset distributed privately.
// Unauthorized copying, distribution, or alteration is strictly prohibited.
// Verification of license required for execution.
use std::f64::consts::PI;

pub struct SonicEngine {
    pub sample_rate: u32,
}

impl SonicEngine {
    pub fn new(sample_rate: u32) -> Self {
        Self { sample_rate }
    }

    /// Genera un bloque de buffer sónico combinando las frecuencias de 432Hz y 528Hz
    pub fn generate_geometry_buffer(&self, size: usize, duration_sec: f64) -> Vec<f64> {
        let mut buffer = Vec::with_capacity(size);
        
        // Frecuencias base del ecosistema Aura
        let freq_aurea: f64 = 432.0;
        let freq_resonante: f64 = 528.0;

        for i in 0..size {
            let t = (i as f64 / self.sample_rate as f64) * duration_sec;
            
            // Ondas sinusoidales puras de geometría armónica
            let wave_432 = (2.0 * PI * freq_aurea * t).sin();
            let wave_528 = (2.0 * PI * freq_resonante * t).sin();
            
            // Interferencia constructiva balanceada (0.5 de amplitud máxima para evitar clipping)
            let combined_signal = (wave_432 + wave_528) * 0.5;
            buffer.push(combined_signal);
        }

        buffer
    }
}
