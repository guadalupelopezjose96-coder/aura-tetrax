# =================================================================
# MAKEFILE MAESTRO: Aura-Tetrax Integración Total
# PROTOCOLO: 100% Debido / Standard 1979
# =================================================================

CC = g++
CFLAGS = -O3 -march=native -ffast-math -pthread -I include
RUST_DIR = src/validation

all: blindaje_rust motor_cpp

blindaje_rust:
	@echo "--- [1/2] Sellando Verdad Digital (Rust) ---"
	cd $(RUST_DIR) && cargo build --release

motor_cpp:
	@echo "--- [2/2] Compilando Motor Geométrico (C++) ---"
	$(CC) $(CFLAGS) src/engine/GeometryEngine.cpp -o tetrax_engine

clean:
	rm -f tetrax_engine
	cd $(RUST_DIR) && cargo clean

run:
	@echo "Ejecutando Validación..."
	./$(RUST_DIR)/target/release/aura-tetrax-validator
	@echo "Ejecutando Motor..."
	./tetrax_engine
