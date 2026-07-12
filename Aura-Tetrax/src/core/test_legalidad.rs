mod activo;
use activo::Activo;

fn main() {
    let valor_ilegal = 0.0;
    
    println!("Iniciando prueba de Ley Irrevocable con valor: {}", valor_ilegal);
    
    match Activo::nuevo(valor_ilegal) {
        Ok(_) => println!("Error: El sistema aceptó un valor ilegal."),
        Err(e) => println!("ÉXITO: El sistema ha bloqueado el valor ilegal. Mensaje: {}", e),
    }
}
