use std::process::Command;

pub fn firmar_log_telemetria(nombre_archivo: &str) -> Result<(), String> {
    let estatus = Command::new("gpg")
        .args(["--batch", "--yes", "--detach-sign", "--armor", nombre_archivo])
        .status()
        .map_err(|e| e.to_string())?;

    if estatus.success() { Ok(()) } else { Err("Error en firma GPG".to_string()) }
}
