pub fn sync_energetico() {
    let temp = obtener_temperatura_sistema();
    
    if temp > 75.0 {
        println!("[ALERTA] Temperatura crítica. Reduciendo a 76 núcleos.");
        limitar_nucleos(76);
    } else {
        println!("[OK] Temperatura óptima. Ejecutando Fusión en 88 núcleos.");
        activar_nucleos(88);
    }
}
