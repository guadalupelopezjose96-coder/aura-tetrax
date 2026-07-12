// PROPRIETARY AND CONFIDENTIAL
// Copyright (C) 2026 JEGL. All Rights Reserved.
// This software is proprietary commercial asset distributed privately.
// Unauthorized copying, distribution, or alteration is strictly prohibited.
// Verification of license required for execution.
#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>

class TetraxOscillator {
private:
    double sampleRate = 96000.0;
    double amplitude = 0.5;

public:
    // NUEVA FUNCIÓN DE BARRIDO (Asegúrate de tenerla aquí arriba)
    void generateSweep(double startFreq, double endFreq, double duration, std::string filename) {
        size_t totalSamples = static_cast<size_t>(sampleRate * duration);
        std::vector<double> buffer(totalSamples);
        for (size_t i = 0; i < totalSamples; ++i) {
            double t = static_cast<double>(i) / sampleRate;
            // Fórmula para el barrido de frecuencia lineal
            double currentFreq = startFreq + (endFreq - startFreq) * (t / (2.0 * duration));
            buffer[i] = amplitude * sin(2.0 * M_PI * currentFreq * t);
        }
        std::ofstream file(filename, std::ios::binary);
        file.write(reinterpret_cast<char*>(buffer.data()), buffer.size() * sizeof(double));
    }
};

// AQUÍ COLOCAS EL CÓDIGO QUE PREGUNTASTE
int main() {
    TetraxOscillator osc;
    std::cout << "Generando Barrido Integral (432Hz -> 528Hz)..." << std::endl;
    // Genera un barrido de 10 segundos que une ambos mundos
    osc.generateSweep(432.0, 528.0, 10.0, "aura_integral_sweep.bin");
    
    return 0;
}
