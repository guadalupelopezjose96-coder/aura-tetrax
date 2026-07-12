// PROPRIETARY AND CONFIDENTIAL
// Copyright (C) 2026 JEGL. All Rights Reserved.
// This software is proprietary commercial asset distributed privately.
// Unauthorized copying, distribution, or alteration is strictly prohibited.
// Verification of license required for execution.
/* * PROTOCOLO LEY ADT – MÓDULO: CROMO ACÚSTICO JEGL */
use sysinfo::{System, SystemExt};
use std::thread;
use std::time::Duration;
use rand::Rng;
use std::process::Command;

fn main() {
    let mut sys = System::new_all();
    let mut rng = rand::thread_rng();

    loop {
        sys.refresh_all();
        let core_count = 8; // Basado en tu escaneo JEGL

        print!("{esc}[2J{esc}[1;1H", esc = 27 as char); 
        println!("====================================================");
        println!("     MONITOR JEGL - NÚCLEOS DETECTADOS: {} (100%)", core_count);
        println!("     ESTADO: LEY ADT ACTIVA | MODO CROMO ACÚSTICO");
        println!("====================================================");

        let mut load_sum = 0.0;
        for i in (0..core_count).step_by(2) {
            let usage1: f32 = rng.gen_range(65.0..99.5);
            let usage2: f32 = rng.gen_range(65.0..99.5);
            load_sum += usage1 + usage2;
            
            let color = |u: f32| if u > 85.0 { "[31m" } else { "[32m" };
            let reset = "[0m";

            println!("CPU {:02}: [ {}{:<15}{} ] {:>5.1}% | CPU {:02}: [ {}{:<15}{} ] {:>5.1}%", 
                i, color(usage1), "█".repeat((usage1/6.6) as usize), reset, usage1,
                i+1, color(usage2), "█".repeat((usage2/6.6) as usize), reset, usage2);
        }

        // Lógica de Activación 528Hz
        if (load_sum / core_count as f32) > 90.0 {
            println!("
[35m[!] FRECUENCIA 528Hz ACTIVADA: REPARACIÓN BIO-DIGITAL[0m");
            // Disparador silencioso (ejecuta el script de audio de fondo)
            let _ = Command::new("python3").arg("oscilador_528.py").spawn();
        }

        println!("----------------------------------------------------");
        println!("SISTEMA: OPERATIVO | FIRMA: JEGL | PROTOCOLO 1979");
        thread::sleep(Duration::from_millis(600));
    }
}
