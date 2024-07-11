import os
import subprocess
from main import *


progres = 0
print("Start")
progres += 10

# Upgrade using winget
subprocess.run(["winget", "upgrade"])
print("winget upgrade: Finished")
progres += 20

# Upgrade all packages using winget
subprocess.run(["winget", "upgrade", "--all"])
print("winget upgrade --all: Finished")
print("Finished upgrade")
progres += 30

# Run chkdsk
subprocess.run(["chkdsk"])
progres += 10

# Run DISM
subprocess.run(["DISM", "/Online", "/Commit-Image", "/Remount-Wim", "/RestoreHealth"])
progres += 30

# Clear the screen (cls)
os.system('cls' if os.name == 'nt' else 'clear')

if progres != 100:
    progres = 100
# Print completion message in green text
print("\033[32mAll Finished\033[0m")

# Pause the script
input("Press Enter to continue...")
    
