from math import fabs
from msilib.schema import Error
from signal import raise_signal
import XboxController
import time
gamepad = XboxController.XboxGamepad()
framesWhereSomethingHappened = 0
def test_joystick():
    global framesWhereSomethingHappened
    for i in range(30 * 4):
        lsx, lsy, rsx, rsy, a, b, x, y, lb, rb, lt, rt = gamepad.read()
        if(lsx, lsy, rsx+ rsy+ a+ b+ x+ y+ lb+ rb+ lt+ rt == 0):
            framesWhereSomethingHappened += 1
        time.sleep(0.25)
    if(framesWhereSomethingHappened != 0):
        raise Exception("Gamepad not found, or no buttons pressed")