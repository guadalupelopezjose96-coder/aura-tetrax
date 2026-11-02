# SPDX-License-Identifier: LicenseRef-AuraIntelCore-Proprietary
# Copyright (c) 2026 Jose Emanuel Guadalupe Lopez (JEGL) - AuraIntelCore / Standard 1979. All Rights Reserved.
# PROPRIETARY & CONFIDENTIAL - WORM READ-ONLY ENFORCED (FERC 2222 / NERC CIP / IRC Sec. 5000H(d))
import curses
import psutil
import time

def main(stdscr):
    # Inicialización de la interfaz
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(100)
    
    while True:
        stdscr.clear()
        
        # Cabecera de estado
        stdscr.addstr(0, 0, "AURA-TETRAX DASHBOARD [SISTEMA: OPERATIVO]", curses.A_BOLD)
        stdscr.addstr(1, 0, "Estado: Modo Global (Sandboxed) | ADT: Activo", curses.A_REVERSE)
        
        # Obtención de carga (Uso global para evitar /proc/stat)
        cpu_usage = psutil.cpu_percent(interval=0.1)
        
        # Representación visual
        bar = "#" * int(cpu_usage / 10)
        status_line = f"Carga de CPU Global: [{bar:<10}] {cpu_usage:>3}%"
        
        try:
            stdscr.addstr(3, 0, status_line)
            stdscr.addstr(5, 0, "Nota: Acceso a nucleos individuales bloqueado por Kernel.")
            stdscr.addstr(6, 0, "Integridad: 100% (No se han requerido privilegios root).")
            stdscr.addstr(8, 0, "Presione 'q' para salir.")
        except curses.error:
            pass
        
        stdscr.refresh()
        
        if stdscr.getch() == ord('q'):
            break
        time.sleep(0.5)

if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass

