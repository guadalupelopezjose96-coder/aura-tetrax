# SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
# Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
# PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
# PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
# PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
# MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
# ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
# 

#!/usr/bin/env python3
import os
import subprocess
import sys

ssh_proxy = os.path.join(os.path.dirname(__file__), "ssh-proxy.py")

argv = [
    os.environ.get("__SSH_PROGRAM_NAME__", "ssh"),
    "-o",
    "ProxyCommand={} %h %p".format(ssh_proxy),
    "-o",
    "Compression=yes",
]

subprocess.call(argv + sys.argv[1:], env=os.environ)
