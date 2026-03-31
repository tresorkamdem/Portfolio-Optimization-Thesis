import subprocess

print("Starte Markowitz...")
subprocess.run(["python", "-m", "scripts.run_markowitz"])

print("\nStarte ML Modell...")
subprocess.run(["python", "-m", "scripts.run_ml"])

print("\nStarte GARCH Modell...")
subprocess.run(["python", "-m", "scripts.run_garch"])