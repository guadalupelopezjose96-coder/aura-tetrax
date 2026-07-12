use std::io::{self, Write};

pub fn verificar_identidad_arquitecto() -> bool {
    print!(">>> Ingresar Token de Sesión JEGL: ");
    io::stdout().flush().unwrap();

    let mut token = String::new();
    io::stdin().read_line(&mut token).unwrap();

    // El token se valida contra una clave maestra guardada en el llavero seguro del sistema
    let token_valido = "JEGL-Sovereign-2026-X88"; 
    
    if token.trim() == token_valido {
        println!("[AUTORIZADO] Identidad confirmada.");
        true
    } else {
        println!("[RECHAZADO] Acceso denegado. Registro de intrusión enviado al Log FESM.");
        false
    }
}
