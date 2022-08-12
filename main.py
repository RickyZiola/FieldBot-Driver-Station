from asyncio.windows_events import NULL
import tkinter as tk
from keyboard import *
import XboxController
from tkinter import ttk


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
    input_label.config(text=str(round(lsx, 2)) + "\n" + str(round(lsy, 2)) + "\n" + str(round(rsx, 2) ) + "\n" + str(round(rsy, 2)) + "\n" + str(round(a, 2) ) + "\n" + str(round(b, 2)) + "\n" + str(round(x, 2) ) + "\n" + str(round(y, 2)) + "\n" + str(round(lb, 2) ) + "\n" + str(round(rb, 2)) + "\n" + str(round(lt, 2) ) + "\n" + str(round(rt, 2)))
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
#sv_ttk.set_theme("dark")
window.attributes('-fullscreen',True)
label = ttk.Label(test, text="Hello World", background="#000000")
label.pack()
close_button = ttk.Button(root, text="Close", command=window.destroy)
close_button.place(rely=1.0, relx=1.0, x=0, y=0, anchor='se')
window.after(500, emergency_exit)
window.after(100, show_input)
window.mainloop()