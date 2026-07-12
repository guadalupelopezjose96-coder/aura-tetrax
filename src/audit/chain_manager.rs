use sha2::{Sha256, Digest};

pub struct ChainManager {
    pub ultimo_hash: String,
}

impl ChainManager {
    pub fn registrar_evento(&mut self, datos: String) -> String {
        let mut hasher = Sha256::new();
        hasher.update(format!("{}{}", self.ultimo_hash, datos));
        let nuevo_hash = format!("{:x}", hasher.finalize());
        self.ultimo_hash = nuevo_hash.clone();
        nuevo_hash
    }
}
