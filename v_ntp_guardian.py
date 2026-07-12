import ntplib
from time import ctime

def verificar_tiempo_soberano():
    c = ntplib.NTPClient()
    try:
        # Consulta a servidores de tiempo de alta precisión
        response = c.request('pool.ntp.org', version=3)
        print(f"[V] Tiempo verificado: {ctime(response.tx_time)}")
        return response.tx_time
    except Exception as e:
        print(f"[!] CRITICAL: Error de sincronización NTP. Acceso a red denegado.")
        # Aquí llamarías a tu función de purga si el tiempo es inalcanzable
        exit(1)

if __name__ == "__main__":
    verificar_tiempo_soberano()
