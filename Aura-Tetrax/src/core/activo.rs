pub struct Activo {
    pub valor: f64,
}

impl Activo {
    pub fn nuevo(valor_input: f64) -> Result<Self, String> {
        // Ejecución de la Ley Irrevocable: El 100% de lo que sea <= 0 es ilegal.
        if valor_input <= 0.0 {
            // Acción: Revocación total de la operación
            return Err("ERROR CRÍTICO: Violación de Ley Irrevocable. Valor nulo o negativo detectado en Activo.".to_string());
        }
        
        Ok(Activo { valor: valor_input })
    }

    pub fn procesar_valor(&self) -> f64 {
        // Garantía de integridad constante
        assert!(self.valor > 0.0, "VIOLACIÓN DE LEY: Se ha detectado un valor no-positivo en el sistema.");
        self.valor
    }
}
