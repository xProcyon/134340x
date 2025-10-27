import os
import time
import subprocess
#ejecutar el code en bash: python3 commit.py
#💡Opcional: si quieres que se ejecute en segundo plano: nohup python3 commit.py &

# Intervalo en segundos (5 minutos = 300 segundos)1	60
#2	120 #3	180 #4	240 #5	300 #6	360
#7	420 #8	480 #9	540 #10	600
INTERVALO = 300  

def ejecutar(comando):
    """Ejecuta un comando y muestra su salida."""
    print(f"\n>>> Ejecutando: {comando}")
    resultado = subprocess.run(comando, shell=True, text=True, capture_output=True)
    if resultado.stdout:
        print(resultado.stdout)
    if resultado.stderr:
        print(resultado.stderr)

contador = 1  # Inicia el contador en 1

while True:
    print("\n==============================")
    print(f"Guardando cambios (Ejecución #{contador})...")
    print("==============================")
    
    ejecutar("git add .")
    ejecutar(f'git commit -m "actualizado (ejecución #{contador})"')
    ejecutar("git pull --rebase")
    ejecutar("git push")
    
    print(f"✅ Cambios guardados (Ejecución #{contador}). Esperando {INTERVALO/60} minutos...\n")
    
    contador += 1
    time.sleep(INTERVALO)