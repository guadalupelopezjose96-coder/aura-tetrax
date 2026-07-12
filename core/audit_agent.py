# core/audit_agent.py
def verificar_integridad_log(ruta_log):
    try:
        with open(ruta_log, 'r') as f:
            lineas = f.readlines()
            # Un sistema sano no debe tener líneas de 'FALLO' o 'INTENTO DE FRAUDE'
            errores = [l for l in lineas if "FALLO" in l or "FRAUDE" in l]
            return {
                "total_transacciones": len(lineas),
                "alertas": len(errores),
                "estado_salud": "CRITICO" if len(errores) > 0 else "OPTIMO"
            }
    except FileNotFoundError:
        return {"estado": "ERROR", "detalle": "Log no encontrado"}
