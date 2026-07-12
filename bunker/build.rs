// PROPRIETARY AND CONFIDENTIAL
// Copyright (C) 2026 JEGL. All Rights Reserved.
// This software is proprietary commercial asset distributed privately.
// Unauthorized copying, distribution, or alteration is strictly prohibited.
// Verification of license required for execution.
/* * PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
 * PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
 * MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
 * ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
 */

// -----------------------------------------------------------------------
// ARQUITECTO DE COMPILACIÓN - JEGL-ELITE v
// AUTORÍA: JEGL (Justicia, Eficiencia, Gestión y Legalidad)
// © 2026 JEGL. 100% LEGAL AL 100%.
// -----------------------------------------------------------------------

fn main() {
    // 1. Monitorea cambios en el escudo para re-compilación inteligente.
    // Si editas el .cpp, Rust lo detectará al 100%.
    println!("cargo:rerun-if-changed=escudo_jegl.cpp");
    
    // 2. Configuración del compilador cc para el blindaje C++
    cc::Build::new()
        .cpp(true)                         // Activa el soporte para C++
        .file("escudo_jegl.cpp")           // Tu archivo de escudo perimetral
        .warnings(true)                    // Excelencia técnica en el reporte
        .flag("-O3")                       // Optimización de nivel v (máximo rendimiento)
        .flag("-std=c++17")                // Estándar de seguridad moderno
        .compile("escudo_jegl");           // Genera la librería estática final

    // 3. Instrucción de enlace para el linker
    println!("cargo:rustc-link-lib=static=escudo_jegl");
    
    println!("✅ Enlace maestro JEGL-Elite configurado al 100%.");
}
