import subprocess, time

note = subprocess.Popen(["gedit"])
print(f"PID: {note.pid}")

time.sleep(3)
note.terminate()