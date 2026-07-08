import subprocess

# Ejecuta los comandos de Git en línea
subprocess.run("git add .", shell=True)
subprocess.run('git commit -m "actualizado"', shell=True)
subprocess.run("git pull --rebase", shell=True)
subprocess.run("git push", shell=True)
