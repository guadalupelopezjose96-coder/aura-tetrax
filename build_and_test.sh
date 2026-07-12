#!/usr/bin/env bash
# ==============================================================================
# PIPELINE AUTOMATIZAT DE COMPILARE ȘI VERIFICARE INTEGRALĂ
# MODUL: build_and_test.sh
# AUTOR: JEGL
# COMPLIANCE: STANDARD 1979 FESM / LEY ADT
# ==============================================================================

set -e # Oprește execuția imediat dacă vreo comandă eșuează

echo "[1/4] Inițializare mediu și curățare artefacte anterioare..."
rm -rf build/ justicia_maxima*.c justicia_maxima*.so

echo "[2/4] Lansare proces de compilare nativă cu Cython (setup.py)..."
python3 setup.py build_ext --inplace

echo "[3/4] Aplicare blindaj structural: Eliminare metadate (strip)..."
BINARY_FILE=$(ls justicia_maxima*.so 2>/dev/null | head -n 1)
if [ -z "$BINARY_FILE" ]; then
    echo "[EROARE] Fișierul binar .so nu a putut fi generat."
    exit 1
fi
strip "$BINARY_FILE"
echo "-> Artefact protejat cu succes: $BINARY_FILE"

echo "[4/4] Execuție suită de teste unitare pe modulul binar..."
python3 -m unittest test_justicia_maxima.py -v

echo "=============================================================================="
echo "PROCES COMPLETAT: SISTEMA GLOBAL INTEGRADO EXITOSAMENTE [100% LEGAL]"
echo "=============================================================================="
