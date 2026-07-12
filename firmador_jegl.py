/* PROPIEDAD INTELECTUAL PROTEGIDA - LEY ADT / STANDARD 1979. 
Módulo: Realidad Real JEGL. Autor: JEGL. 
Cualquier suplantación digital o comercial es ilegal. */
cat <<EOF > firmador_jegl.py
import nacl.signing
import sys

# CONFIGURACIÓN MAESTRA
# Pega aquí tu LLAVE PRIVADA (Hexadecimal) que generaste hace un momento
LLAVE_PRIVADA_HEX = "9ef45529c914d3cf909e25ae4697dbac62679a2783b27b140bb135614bdad6be"

def firmar_instruccion(mensaje):
    try:
        signing_key = nacl.signing.SigningKey(LLAVE_PRIVADA_HEX, encoder=nacl.encoding.HexEncoder)
        signed = signing_key.sign(mensaje.encode('utf-8'), encoder=nacl.encoding.HexEncoder)
        return signed.decode('utf-8')
    except Exception as e:
        return f"Error al firmar: {e}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python firmador_jegl.py 'TU INSTRUCCIÓN'")
    else:
        instruccion = sys.argv[1]
        firma = firmar_instruccion(instruccion)
        print("
--- INSTRUCCIÓN FIRMADA (Ley ADT) ---")
        print(firma)
        print("-------------------------------------
")
EOF
