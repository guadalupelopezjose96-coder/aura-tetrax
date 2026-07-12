use std::process::Command;

pub fn activar_lockdown() {
    println!("[!] ALERTA: INTENTO DE ACCESO NO AUTORIZADO DETECTADO.");
    println!("[!] Iniciando protocolo de Lockdown...");

    // Revocar permisos de escritura y lectura de los scripts críticos
    Command::new("chmod")
        .args(["-R", "000", "/home/user/scripts/"])
        .status()
        .expect("Error al ejecutar Lockdown.");

    // Registrar en FESM
    Command::new("logger")
        .arg("CRÍTICO: Acceso no autorizado. Sistema en modo Lockdown.")
        .status()
        .ok();
}
