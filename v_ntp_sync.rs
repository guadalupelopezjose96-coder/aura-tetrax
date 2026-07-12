// Módulo de Validación de Tiempo (Fail-Closed)
use std::time::Duration;
use ntp_client::NtpClient; // Librería de alto rendimiento

pub fn check_time_integrity() -> bool {
    let client = NtpClient::new("pool.ntp.org:123");
    
    // Si el servidor NTP no responde tras 3 segundos, el sistema se bloquea.
    match client.get_time_timeout(Duration::from_secs(3)) {
        Ok(ntp_time) => {
            // Comparar ntp_time contra el timestamp codificado en el token
            validate_against_license(ntp_time)
        },
        Err(_) => {
            // El "Fail-Closed": si no hay NTP, no hay ejecución.
            println!("CRITICAL: Fallo de sincronización. Conecte Aura-Tetrax a la red.");
            std::process::exit(1); 
        }
    }
}
