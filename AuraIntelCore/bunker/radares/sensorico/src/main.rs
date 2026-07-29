# ==============================================================================
# LEY ADT - AUDITORIA, DOMINIO Y TRANSMUTACION
# Propiedad Intelectual Abandono / Licencia Soberana JEGL
# ==============================================================================

use sha2::{Sha256, Digest};
use chrono::Utc;
use std::io::{self, Write};

// Estructura 100% legal para el registro inmutable (Law-as-Code)
struct RegistroSensorico {
    timestamp: String,
    frecuencia_detectada_hz: f64,
    hash_inmutable: String,
    estatus_legal: String,
}

fn main() {
    println!("============================================================");
    println!(" RADAR SENSÓRICO DIGITAL - NODO DE CAPTURA DISTRIBUIDA");
    println!(" ARQUITECTO TÉCNICO: JEGL");
    println!(" ESTATUS: 100% PROPIEDAD PRIVADA");
    println!(" AUTOMATIZACIÓN: DESACTIVADA (EJECUCIÓN 100% MANUAL)");
    println!("============================================================");

    // Requiere intervención 100% manual para iniciar el escaneo
    print!("> Autorizar escaneo manual de frecuencias (escribe '100' para iniciar): ");
    io::stdout().flush().unwrap();
    
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    // Verificación de la instrucción manual
    if input.trim() == "100" {
        ejecutar_captura_manual();
    } else {
        println!("Escaneo abortado. Se requiere autorización manual al 100%.");
    }
}

fn ejecutar_captura_manual() {
    println!("\n[+] Iniciando captura de espectro sónico y métricas físicas al 100%...");
    
    // Aquí se conectan los osciladores de hardware para leer el entorno.
    // Simulamos la captura de frecuencias clave del entorno para el análisis:
    let frecuencias_capturadas = [432.0, 528.0, 1024.5]; 

    for &frecuencia in frecuencias_capturadas.iter() {
        // 1. Capturar el momento exacto
        let timestamp_actual = Utc::now().to_rfc3339();
        
        // 2. Acoplar los datos crudos para la firma legal
        let datos_crudos = format!("{}-{}", timestamp_actual, frecuencia);
        
        // 3. Generar el Hash Criptográfico (Law-as-Code)
        let mut hasher = Sha256::new();
        hasher.update(datos_crudos.as_bytes());
        let hash_result = format!("{:x}", hasher.finalize());

        let registro = RegistroSensorico {
            timestamp: timestamp_actual,
            frecuencia_detectada_hz: frecuencia,
            hash_inmutable: hash_result,
            estatus_legal: String::from("100% DEBIDO Y LEGAL"),
        };

        validar_y_registrar(registro);
    }
    
    println!("\n[+] Captura 100% completada. Datos asegurados en la memoria local del nodo.");
}

fn validar_y_registrar(registro: RegistroSensorico) {
    println!("------------------------------------------------------------");
    println!("TIMESTAMP: {}", registro.timestamp);
    println!("FRECUENCIA: {} Hz", registro.frecuencia_detectada_hz);
    
    // Validación de Geometría Sónica y Cromo Acústica
    if registro.frecuencia_detectada_hz == 432.0 || registro.frecuencia_detectada_hz == 528.0 {
        println!("ANÁLISIS: Frecuencia de Geometría Sónica ALINEADA al 100%");
    }
    
    println!("HASH (VERDAD DIGITAL): {}", registro.hash_inmutable);
    println!("ESTATUS OPERATIVO: {}", registro.estatus_legal);
}
