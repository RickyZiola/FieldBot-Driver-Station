from asyncio.windows_events import NULL
import tkinter as tk
from keyboard import *
import XboxController
from tkinter import ttk
import numpy as math

confWindow = NULL

# Function to close Driver Station

def exit_ds():
    global confWindow

    confWindow = tk.Tk()  # Create a conformation window

    confWindow.title("Close Driver Station?")    # Title the window

    confWindow.geometry("300x100")    # Resize and position the window
    confWindow.eval('tk::PlaceWindow . center')

    confWindow.tk.call("source", "Azure-ttk-theme/azure.tcl")  
    confWindow.tk.call("set_theme", "dark")     # Add the theme to the window

    confRoot = ttk.Frame(confWindow)   # Create a frame for the window
    confRoot.pack(fill="both", expand=True)

    label = ttk.Label(confRoot, text="Close Driver Station?", font=("arial", 20, "bold"))
    label.pack()      # Create a prompt to close the DS

    yesButton = ttk.Button(confRoot, text="Confirm", style="Accent.TButton", command=close)
    yesButton.place(rely=1.0, relx=0.0, x=0, y=0, anchor='sw')      # Create a Confirm button

    noButton = ttk.Button(confRoot, text="Cancel", style="TButton", command=confWindow.destroy)
    noButton.place(rely=1.0, relx=1.0, x=0, y=0, anchor='se')       # Create a Cancel button

    confWindow.mainloop()   # Run the window

def close():    # Close the main a conformation windows
    window.destroy()
    confWindow.destroy()

# Function declaration for bad scenarios

esc_was_pressed = False
def emergency_exit():   # In the event of a bug in the driver station, you can hold down ESC to close it
    global esc_was_pressed
    if(esc_was_pressed and is_pressed("esc")):
        window.destroy()
    esc_was_pressed = is_pressed("esc")
    root.after(500, emergency_exit)

def robot_kill():       # In the event of a robot software bug, press ENTER to kill all movement
    pass  # will be implemented with radio

# Function declaration for input handling
joystick = XboxController.XboxGamepad()
def show_input():
    lsx, lsy, rsx, rsy, a, b, x, y, lb, rb, lt, rt = joystick.read()
    input_label.config(text=str(math.piecewise(round(lsx, 2), [abs(round(lsx, 2)) < 0.05, abs(round(lsx, 2)) >= 0.05], [0, round(lsx, 2)])) + "\n" + str(math.piecewise(round(lsy, 2), [abs(round(lsx, 2)) < 0.05, abs(round(lsy, 2)) >= 0.05], [0, round(lsy, 2)])) + "\n" + str(math.piecewise(round(rsx, 2), [abs(round(rsx, 2)) < 0.05, abs(round(rsx, 2)) >= 0.05], [0, round(rsx, 2)])) + "\n" + str(math.piecewise(round(rsy, 2), [abs(round(rsy, 2)) < 0.05, abs(round(rsy, 2)) >= 0.05], [0, round(rsy, 2)])) + "\n" + str(round(a, 2) ) + "\n" + str(round(b, 2)) + "\n" + str(round(x, 2) ) + "\n" + str(round(y, 2)) + "\n" + str(round(lb, 2) ) + "\n" + str(round(rb, 2)) + "\n" + str(round(lt, 2) ) + "\n" + str(round(rt, 2)))
    input_label.update_idletasks()
    root.after(100, show_input)

window = tk.Tk()
window.tk.call("source", "Azure-ttk-theme/azure.tcl")
window.tk.call("set_theme", "dark")
root = ttk.Frame(window)
root.pack(fill="both", expand=True)

s = ttk.Style()
s.configure('new.TFrame', background='#000000')
test = ttk.Frame(root, style='new.TFrame')
test.pack()
input_label = ttk.Label(test, text='', background="#000000")
input_label.pack()
window.attributes('-fullscreen',True)
label = ttk.Label(test, text="Hello World", background="#000000")
label.pack()
s.configure("new.TButton", font=("arial", 20))
close_button = ttk.Button(root, text="Close", command=exit_ds, style="new.TButton")
close_button.place(rely=1.0, relx=1.0, x=0, y=0, anchor='se')
window.after(500, emergency_exit)
window.after(100, show_input)
window.mainloop()