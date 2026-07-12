# --- Makefile Maestro para Aura-Tetrax (Arquitectura Rust) ---
# Optimización 100% para el motor de geometría sónica

# Definición de variables de entorno
CARGO := cargo
RELEASE_DIR := target/release
BINARY := aura_engine # Ajusta este nombre al definido en tu Cargo.toml

all: build

# Compilación en modo release para máximo rendimiento sónico
build:
	@echo "Iniciando compilación sónica... [Status: 100%]"
	$(CARGO) build --release
	@echo "Compilación exitosa. Binario disponible en $(RELEASE_DIR)/"

# Ejecución del sistema
run:
	@echo "Ejecutando Aura-Tetrax... [Status: 100%]"
	$(CARGO) run --release

# Limpieza total para mantener la soberanía del entorno
clean:
	@echo "Ejecutando protocolo de limpieza... [Status: 100%]"
	$(CARGO) clean
	@rm -rf bin/

# Auditoría de integridad (Conexión con tu script de soberanía)
audit:
	@echo "Iniciando auditoría de soberanía... [Status: 100%]"
	@chmod +x audit_soberania.sh
	@./audit_soberania.sh

.PHONY: all build run clean audit
