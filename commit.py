import os
import time
import subprocess

# Intervalo en segundos (5 minutos = 300 segundos)
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