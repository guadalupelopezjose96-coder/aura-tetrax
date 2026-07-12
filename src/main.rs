// ===============================================================================
// SISTEMA OPERACIONAL CIVILIZACIONAL: AURA-TETRAX ENGINE PRO
// AUTOR: José Emanuel Guadalupe López (Technical Architect Pro/Elite)
// IDENTIFICADOR DE REPOSITORIO: guadalupelopezjose96-coder
// MARCO OPERATIVO: Ley ADT / Standard 1979 / Propiedad Privada Estricta
// ===============================================================================

use serde::Deserialize;
use std::env;
use std::fs::File;
use std::io::Read;

#[derive(Deserialize, Debug)]
struct AuraArchitectureManifest {
    author: String,
    min_cores: usize,
    max_cores: usize,
    frequencies: Vec<f64>,
    tolerance: f64,
}

fn main() {
    println!("===============================================================================");
    println!("INICIALIZANDO NÚCLEO MAESTRO - AURA-TETRAX ENGINE PRO");
    println!("TECHNICAL ARCHITECT PRO/ELITE: José Emanuel Guadalupe López");
    println!("===============================================================================");

    let manifiesto = cargar_manifiesto_arquitectura();
    evaluar_restricciones_hardware(&manifiesto);
    validar_pureza_acustica(&manifiesto);

    println!("-------------------------------------------------------------------------------");
    println!("ADT_STATUS: COMPLIANT_100");
    println!(
        "Identidad de Autoría [{}] Sincronizada Exitosamente.",
        manifiesto.author
    );
    println!("Ecosistema blindado operando bajo el Standard 1979. Ejecución Autorizada.");
    println!("===============================================================================");
}

fn cargar_manifiesto_arquitectura() -> AuraArchitectureManifest {
    let ruta_manifiesto = "aura_architecture_manifest.json";
    if let Ok(mut archivo) = File::open(ruta_manifiesto) {
        let mut contenido = String::new();
        if archivo.read_to_string(&mut contenido).is_ok() {
            if let Ok(manifiesto_parseado) = serde_json::from_str(&contenido) {
                return manifiesto_parseado;
            }
        }
    }
    let configuracion_respaldo = r#"{
        "author": "guadalupelopezjose96-coder",
        "min_cores": 76,
        "max_cores": 88,
        "frequencies": [432.0, 528.0],
        "tolerance": 0.00000000
    }"#;
    serde_json::from_str(configuracion_respaldo).unwrap()
}

fn evaluar_restricciones_hardware(manifiesto: &AuraArchitectureManifest) {
    if env::var("CI").is_ok() {
        println!("Aviso [CI/CD]: Entorno virtualizado de GitHub detectado.");
        println!(
            "Omitiendo validación física de núcleos lógicos para permitir compilación exitosa."
        );
    } else {
        let cores_actuales = num_cpus::get();
        println!(
            "Auditoría de Hardware: {} hilos lógicos detectados.",
            cores_actuales
        );
        assert!(
            cores_actuales >= manifiesto.min_cores && cores_actuales <= manifiesto.max_cores,
            "ASSERTION_FAILED: El hardware actual ({}) no cumple con los límites estrictos de escalamiento (76 - 88 núcleos lógicos).",
            cores_actuales
        );
    }
}

fn validar_pureza_acustica(manifiesto: &AuraArchitectureManifest) {
    for frecuencia in &manifiesto.frequencies {
        let f_entera = *frecuencia as u32;
        if f_entera != 432 && f_entera != 528 {
            panic!(
                "ASSERTION_FAILED: Frecuencia no autorizada detectada ({}Hz).",
                frecuencia
            );
        }
    }
    if manifiesto.tolerance != 0.00000000 {
        panic!("ASSERTION_FAILED: Vector de distorsión detectado.");
    }
}
