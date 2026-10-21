import os
import subprocess
if os.name == 'nt':
    subprocess.run("dir")
elif os.name == 'posix':
    subprocess.run("ls")