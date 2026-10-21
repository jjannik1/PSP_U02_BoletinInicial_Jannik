import subprocess

try:
    subprocess.run(["ping", "-c","3","8.8.8.8"],capture_output=True, text=True, timeout=1)

except subprocess.TimeoutExpired:
    print("Timeout")