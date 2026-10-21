import subprocess
from time import sleep

calc = subprocess.Popen("gnome-calculator")
print(f"{calc.pid}")
sleep(2)
calc.terminate()