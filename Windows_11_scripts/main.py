import tkinter as tk
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
import subprocess
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
screen_width = screen.winfo_screenwidth()
screen_height = screen.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

screen.geometry(f"{window_width}x{window_height}+{center_x}+{center_y - 100}")
is_dark = False
bgColor = "#FFFFFF"

# Load and configure the image for the button
image_path = r"C:\Users\User\Desktop\code\Windows_11_scripts\images\LD.ico"
image = Image.open(image_path)
LD_photo = ImageTk.PhotoImage(image)

class Progress_bar:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.progress_bar_screen = None
        self.progress = None

    def progress_bar_start(self):
        if self.progress_bar_screen is not None:
            return  # Progress bar is already running

        # Create the progress bar window
        self.progress_bar_screen = tk.Toplevel(screen)
        self.progress_bar_screen.title("Progress Bar")
        self.progress_bar_screen.resizable(False, False)
        self.progress_bar_screen.geometry(f"{300}x100+{self.x}+{self.y}")

        # Create the progress bar widget
        self.progress = Progressbar(self.progress_bar_screen, orient="horizontal", length=275, mode='determinate')
        self.progress.pack(pady=10)
        self.progress['maximum'] = 100
        self.progress['value'] = 0

    def progress_bar_stop(self):
        if self.progress_bar_screen is not None:
            self.progress_bar_screen.destroy()
            self.progress_bar_screen = None

    def update_progress_bar(self, value):
        if self.progress['value'] >= 100:
            self.progress['value'] += value
            self.progress_bar_screen.update_idletasks()

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

def run_script_chkdsk():
    progress_bar.progress_bar_start()  # Start the progress bar

    for i in range(0, 101, 20):
        progress_bar.update_progress_bar(20)
        screen.after(500)  # Simulate some work being done

    subprocess.run(["python", r"C:\Users\User\Desktop\code\Windows_11_scripts\chkdek.py"])  # Run the script using subprocess module

    progress_bar.progress_bar_stop()  # Stop the progress bar

def long_running_task(progress_bar):
    """Simulate a long-running task"""
    for i in range(101):
        time.sleep(0.05)  # Simulate work being done
        progress_bar['value'] = i  # Update progress bar value
    progress_bar.destroy()  # Remove the progress bar once done

def start_task():
    """Start the long-running task in a separate thread"""
    progress_bar = ttk.Progressbar(screen, mode='determinate', length=200)
    progress_bar.grid(row=1, column=0, pady=20)
    progress_bar['value'] = 0

    # Run the long-running task in a separate thread
    task_thread = threading.Thread(target=long_running_task, args=(progress_bar,))
    task_thread.start()


def pb():
    progress_bar.progress_bar_start()

    for value in [10, 2, 56]:
        progress_bar.update_progress_bar(value)
        time.sleep(1)

    progress_bar.progress_bar_stop()

# Create a progress bar instance
progress_bar = Progress_bar(center_x, center_y)

button = tk.Button(screen, text="Lait Dark", command=long_running_task, borderwidth=0)
button.place(x=center_x, y=center_y)

# Create a button widget
LD_button = tk.Button(screen, text="Lait Dark", command=on_button_click_Lait_Dark, image=LD_photo, borderwidth=0)
LD_button.place(x=25, y=25)  # Set button position to (25, 25)

# Create a label in the center of the screen with the custom font
label = tk.Label(screen, text="All in one Windows 11 scripts", font="Terminal", borderwidth=0)
label.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=-200)

# Create a button to run script
button_chkdsk = tk.Button(screen, text="Run script", command=run_script_chkdsk, borderwidth=0)
button_chkdsk.place(x=25, y=75)  # Set button position to (25, 75)

# Start the main event loop
screen.mainloop()
