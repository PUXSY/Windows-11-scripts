import os
import subprocess
from main import *


print("Start")
progress_bar.update_progress_bar(10)

# Upgrade using winget
subprocess.run(["winget", "upgrade"])
print("winget upgrade: Finished")
progress_bar.update_progress_bar(10)

# Upgrade all packages using winget
subprocess.run(["winget", "upgrade", "--all"])
print("winget upgrade --all: Finished")
print("Finished upgrade")
progress_bar.update_progress_bar(30)

# Run chkdsk
subprocess.run(["chkdsk"])
progress_bar.update_progress_bar(10)

# Run DISM
subprocess.run(["DISM", "/Online", "/Commit-Image", "/Remount-Wim", "/RestoreHealth"])
progress_bar.update_progress_bar(40)

# Clear the screen (cls)
os.system('cls' if os.name == 'nt' else 'clear')
    
# Print completion message in green text
print("\033[32mAll Finished\033[0m")

if progress_bar['value'] != 100:
    progress_bar['value'] = 100
    progress_bar.progress_bar_screen.update_idletasks() 

progress_bar.progress_bar_screen.update_idletasks() 
# Pause the script
input("Press Enter to continue...")
    
