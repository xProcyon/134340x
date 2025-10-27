import os
import time
import subprocess
#python3 commit.py

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

while True:
    print("\n==============================")
    print("Guardando cambios en el repositorio...")
    print("==============================")
    
    ejecutar("git add .")
    ejecutar('git commit -m "actualizado"')
    ejecutar("git pull --rebase")
    ejecutar("git push")
    
    print("✅ Cambios guardados. Esperando 5 minutos...\n")
    time.sleep(INTERVALO)