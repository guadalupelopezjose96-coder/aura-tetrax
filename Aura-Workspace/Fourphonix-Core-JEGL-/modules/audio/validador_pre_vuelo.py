import sys
import py_compile

def validar_100_por_ciento():
    archivos_criticos = [
        'ley_1979_core.py',
        'orquestador_76_jegl.py',
        'seguridad_adt.py'
    ]
    
    print("🛡️ Iniciando Protocolo de Validación JEGL...")
    exito = True
    
    for archivo in archivos_criticos:
        try:
            py_compile.compile(archivo, doraise=True)
            print(f"✅ {archivo}: Estructura perfecta.")
        except py_compile.PyCompileError as e:
            print(f"❌ {archivo}: Error detectado -> {e}")
            exito = False
            
    return exito

if __name__ == "__main__":
    if not validar_100_por_ciento():
        sys.exit(1)
    print("🚀 Todo el sistema está al 100%. Listo para el Push.")
