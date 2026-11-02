// SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
// Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
// PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
pub mod adt;

use crate::core::adt::{ejecutar_logica_fiscal_adt, ActoJuridico};
use ed25519_dalek::SigningKey; // Importación actualizada a v2.2.0
use rayon::prelude::*;
use std::sync::{Arc, Mutex};
use std::fs::File;
use std::io::Write;
use serde::{Serialize, Deserialize};

pub struct HexakisEngine {
    pub nombre_motor: String,
    pub clave_soberana: SigningKey, // Tipo actualizado
    pub registro_auditoria: Arc<Mutex<Vec<ActoJuridico>>>,
}

impl HexakisEngine {
    pub fn new(signing_key: SigningKey) -> Self {
        Self {
            nombre_motor: String::from("Hexakis-Pro-Elite"),
            clave_soberana: signing_key,
            registro_auditoria: Arc::new(Mutex::new(Vec::new())),
        }
    }

    pub fn procesar_lote_fiscal(&self, datos: Vec<String>) {
        let resultados: Vec<ActoJuridico> = datos.into_par_iter()
            .map(|d| {
                ejecutar_logica_fiscal_adt(&d, &self.clave_soberana)
                    .expect("Fallo en la Ley ADT: Integridad comprometida")
            })
            .collect();

        let mut registro = self.registro_auditoria.lock().unwrap();
        registro.extend(resultados);
    }

    pub fn guardar_registro_en_disco(&self, ruta: &str) -> anyhow::Result<()> {
        let registro = self.registro_auditoria.lock().unwrap();
        let encoded: Vec<u8> = bincode::serialize(&*registro)?;
        
        let mut file = File::create(ruta)?;
        file.write_all(&encoded)?;
        Ok(())
    }
}
