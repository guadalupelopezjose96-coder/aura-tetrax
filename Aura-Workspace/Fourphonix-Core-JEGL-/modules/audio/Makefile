# Makefile - Tetrax Engine Pro (Full Automation)
# Standard 1979 - Maximisisisima Justicia

CXX = g++
CXXFLAGS = -O3 -march=native -Wall -std=c++17
TARGET = tetrax_oscillator
SRCS = oscillator_core.cpp

all: $(TARGET)

$(TARGET): $(SRCS)
	$(CXX) $(CXXFLAGS) $(SRCS) -o $(TARGET)
	@echo "Compilación exitosa."

# Ejecuta, valida y sube a GitHub en una sola cadena
deploy: all
	./$(TARGET)
	@python3 validate_audio.py
	git add .
	git commit -m "Update: Tetrax Audio Core - Frecuencias Validadas $(shell date)"
	git push origin main
	@echo "Despliegue y validación al 100% completados."

clean:
	rm -f $(TARGET) *.bin
	@echo "Entorno limpio."
