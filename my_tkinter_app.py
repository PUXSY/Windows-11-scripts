import tkinter as tk
import os

# Create the main window first
screen = tk.Tk()
screen.title("Windows 11 scripts")
screen.iconbitmap(r"C:\Users\User\Desktop\code\Windows_11_scripts\Untitled.ico")
screen.resizable(False, False)

window_width = 750
window_height = 500
screen_width = screen.winfo_screenwidth()
screen_height = screen.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

screen.geometry(f"{window_width}x{window_height}+{center_x}+{center_y - 100}")
is_dark = False
bgCaler = "#FFFFFF"

# Function to be called when button is clicked
def on_button_click():
    global is_dark
    global bgCaler
    if is_dark:
        bgCaler = "#FFFFFF"
    else:
        bgCaler = "#202020"

    if is_dark:
        screen.config(bg=bgCaler)
        label.config(bg="#FFFFFF", fg="#000000")
    else:
        screen.config(bg=bgCaler)
        label.config(bg="#202020", fg="#007FFF")
    is_dark = not is_dark

def run_script_chkdek():
    os.system(r"C:\Users\User\Desktop\code\Windows_11_scripts\chkdek.cmd") 

# Create a button widget
button = tk.Button(screen, text="Lait Dark", command=on_button_click)
button.place(x=25, y=25)  # Set button position to (25, 25)

# Create a label in the center of the screen with the custom font
label = tk.Label(screen, text="All in one Windows 11 scripts", font="Terminal", borderwidth=0)
label.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=-200)

# Create a button to run script
button_chkdek = tk.Button(screen, text="Run script", command=run_script_chkdek)
button_chkdek.place(x=25, y=75)  # Set button position to (25, 75)

# Start the main event loop
screen.mainloop()
