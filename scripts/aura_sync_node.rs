use std::process::Command;

pub fn replicar_estado_soberano(nodo_destino: &str) {
    println!("[SYNC] Iniciando réplica inmutable hacia: {}", nodo_destino);
    
    // El respaldo se realiza mediante rsync con cifrado SSH
    let status = Command::new("rsync")
        .args(["-avz", "--checksum", "./scripts/", format!("user@{}:/home/user/scripts/", nodo_destino)])
        .status()
        .expect("ERROR: Fallo en la sincronización de soberanía.");

    if status.success() {
        println!("[OK] Nodo {} sincronizado. Soberanía replicada.", nodo_destino);
    }
}
