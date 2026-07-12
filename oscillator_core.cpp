// PROPRIETARY AND CONFIDENTIAL
// Copyright (C) 2026 JEGL. All Rights Reserved.
// This software is proprietary commercial asset distributed privately.
// Unauthorized copying, distribution, or alteration is strictly prohibited.
// Verification of license required for execution.
#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>

// Standard 1979 - Ley ADT
class TetraxOscillator {
private:
    double sampleRate = 96000.0; // Calidad de estudio
    double amplitude = 0.5;

public:
    void generateTone(double frequency, double duration, std::string filename) {
        size_t totalSamples = static_cast<size_t>(sampleRate * duration);
        std::vector<double> buffer(totalSamples);

        for (size_t i = 0; i < totalSamples; ++i) {
            // Generación de onda pura sin aliasing
            buffer[i] = amplitude * sin(2.0 * M_PI * frequency * i / sampleRate);
        }

        // Exportación directa a binario para integridad 100%
        std::ofstream file(filename, std::ios::binary);
        file.write(reinterpret_cast<char*>(buffer.data()), buffer.size() * sizeof(double));
    }
};

int main() {
    TetraxOscillator osc;
    std::cout << "Generando frecuencia de 528Hz (Bio-Digital)..." << std::endl;
    osc.generateTone(528.0, 5.0, "aura_528.bin");
    
    std::cout << "Generando frecuencia de 432Hz (Armonía)..." << std::endl;
    osc.generateTone(432.0, 5.0, "aura_432.bin");
    
    return 0;
}
