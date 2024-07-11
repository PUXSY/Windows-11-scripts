import tkinter as tk
from PIL import Image, ImageTk
import os
import time
from tkinter import ttk
import threading

# Create the main window first
screen = tk.Tk()
screen.title("Windows 11 scripts")
screen.iconbitmap(r"C:\Users\User\Desktop\code\Windows_11_scripts\images\Untitled.ico")
screen.resizable(False, False)


window_width = 750
window_height = 500
center_x = int(window_width / 2)
center_y = int(window_height / 2)

screen.geometry(f"{window_width}x{window_height}+{center_x}+{center_y - 100}")
is_dark = False
bgColor = "#FFFFFF"


# Load and configure the image for the button
image_path = r"C:\Users\User\Desktop\code\Windows_11_scripts\images\LD.ico"
image = Image.open(image_path)
LD_photo = ImageTk.PhotoImage(image)

# Function to be called when button is clicked
def on_button_click_Lait_Dark():
    global is_dark, bgColor

    if is_dark:
        bgColor = "#FFFFFF"
    else:
        bgColor = "#202020"

    screen.config(bg=bgColor)
    label.config(bg=bgColor, fg="#000000" if is_dark else "#007FFF")
    LD_button.config(bg=bgColor, fg="#000000" if is_dark else "#007FFF")

    is_dark = not is_dark

def advance_progress(progress_bar, progress_var, amount):
    """Advance the progress bar by a specific amount"""
    progress_var.set(progress_var.get() + amount)
    progress_bar.update_idletasks()

def long_running_task(progress_bar, progress_var):
    """Run the task and update progress"""
    print("Start")
    advance_progress(progress_bar, progress_var, 10)
    
    # Upgrade using winget
    os.system("winget upgrade")
    print("winget upgrade: Finished")
    advance_progress(progress_bar, progress_var, 20)

    # Upgrade all packages using winget
    os.system("winget upgrade --all")
    print("winget upgrade --all: Finished")
    print("Finished upgrade")
    advance_progress(progress_bar, progress_var, 30)

    # Run chkdsk
    os.system("chkdsk")
    advance_progress(progress_bar, progress_var, 10)

    # Run DISM
    os.system("DISM /Online /Commit-Image /Remount-Wim /RestoreHealth")
    advance_progress(progress_bar, progress_var, 30)

    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    advance_progress(progress_bar, progress_var, 10)
    print("\033[32mAll Finished\033[0m")
    
    # Pause the script
    progress_bar.destroy()  # Remove the progress bar once don


def start_task():
    """Start the long-running task in a separate thread"""
    global progress_bar, progress_var
    progress_var = tk.IntVar()
    progress_bar = ttk.Progressbar(screen, mode='determinate', length=200, variable=progress_var)
    progress_bar.place(x=center_x - 100, y=center_y - 250)
    progress_bar['value'] = 0

    # Run the long-running task in a separate thread
    task_thread = threading.Thread(target=long_running_task, args=(progress_bar, progress_var))
    task_thread.start()



# Create a progress bar instance
start_button = tk.Button(screen, text="Start Task", command=start_task)
start_button.place(x=center_x, y=center_y)


# Create a button widget
LD_button = tk.Button(screen, text="Lait Dark", command=on_button_click_Lait_Dark, image=LD_photo, borderwidth=0)
LD_button.place(x=25, y=25)  # Set button position to (25, 25)

# Create a label in the center of the screen with the custom font
label = tk.Label(screen, text="All in one Windows 11 scripts", font="Terminal", borderwidth=0)
label.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=-200)


# Start the main event loop
screen.mainloop()

    

if screen.destroy() == True:
    progress_bar.quit()
    os.system("exit")
