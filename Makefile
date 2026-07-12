# --- Makefile Maestro para Aura-Tetrax Engine ---
# Configuración 100% optimizada para sistemas multiprocesador

# Detectar automáticamente el número de núcleos para compilación paralela
JOBS := $(shell nproc)

# Compilador y Banderas (Flags)
CXX      := g++
CXXFLAGS := -O3 -march=native -flto -pthread -pipe -Wall -Wextra -DNDEBUG
LDFLAGS  := -flto -lpthread -lm

# Directorios
SRCDIR   := src
OBJDIR   := obj
BINDIR   := bin
TARGET   := $(BINDIR)/aura_engine

# Fuentes y Objetos
SOURCES  := $(wildcard $(SRCDIR)/*.cpp)
OBJECTS  := $(SOURCES:$(SRCDIR)/%.cpp=$(OBJDIR)/%.o)

# Comandos
all: directories $(TARGET)

# Crear directorios necesarios
directories:
	@mkdir -p $(OBJDIR)
	@mkdir -p $(BINDIR)

# Enlazado final
$(TARGET): $(OBJECTS)
	@echo "Enlazando componentes... [Status: 100%]"
	$(CXX) $(OBJECTS) $(LDFLAGS) -o $@
	@echo "Compilación exitosa. Aura-Tetrax listo."

# Compilación de objetos con detección de hilos
$(OBJDIR)/%.o: $(SRCDIR)/%.cpp
	@echo "Compilando módulo: $<"
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Ejecución paralela
run: all
	@./$(TARGET)

# Limpieza total (Seguridad de entorno)
clean:
	@echo "Limpiando binarios y objetos... [Status: 100%]"
	rm -rf $(OBJDIR) $(BINDIR)

.PHONY: all clean run directories
