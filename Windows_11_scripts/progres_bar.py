import tkinter as tk
from tkinter import ttk
import time
import threading

def long_running_task(progress_bar):
    """Simulate a long-running task"""
    for i in range(101):
        time.sleep(0.05)  # Simulate work being done
        progress_bar['value'] = i  # Update progress bar value
    progress_bar.destroy()  # Remove the progress bar once done

def start_task():
    """Start the long-running task in a separate thread"""
    progress_bar = ttk.Progressbar(root, mode='determinate', length=200)
    progress_bar.grid(row=1, column=0, pady=20)
    progress_bar['value'] = 0

    # Run the long-running task in a separate thread
    task_thread = threading.Thread(target=long_running_task, args=(progress_bar,))
    task_thread.start()

# Create the main window
root = tk.Tk()
root.title("Progress Bar Example")

# Create and place the button
start_button = tk.Button(root, text="Start Task", command=start_task)
start_button.grid(row=0, column=0, pady=20)

# Start the main event loop
root.mainloop()