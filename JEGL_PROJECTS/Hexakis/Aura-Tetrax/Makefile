# Makefile Maestro Aura-Tetrax - 100% Legal
CC = g++
CFLAGS = -O3 -march=native -ffast-math -pthread
RUST_DIR = src/validation

all: compile_rust compile_cpp

compile_rust:
	@echo "Compilando Validador Aura (Rust)..."
	cd $(RUST_DIR) && cargo build --release

compile_cpp:
	@echo "Compilando Motor Tetrax (C++)..."
	$(CC) $(CFLAGS) src/engine/*.cpp -o tetrax_engine

clean:
	rm -rf tetrax_engine
	cd $(RUST_DIR) && cargo clean
