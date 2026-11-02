// SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
// Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
// PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
#ifndef AURABRIDGE_HPP
#define AURABRIDGE_HPP

#include <string>

struct ProtocoloJEGL {
    bool integridad_100;
    double frecuencia_actual; // 432.0 o 528.0
    char firma_legal[64];
};

#endif
