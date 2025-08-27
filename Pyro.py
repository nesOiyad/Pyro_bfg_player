import mss
from pynput import mouse
import subprocess
import time

def is_red(pixel, tolerance=10):
    r, g, b = pixel
    return abs(r - 201) <= tolerance and abs(g - 0) <= tolerance and abs(b - 0) <= tolerance

def on_click(x, y, button, pressed):
    if pressed and button == mouse.Button.right:
        with mss.mss() as sct:
            monitor = {"top": 841, "left": 1156, "width": 1, "height": 1}
            pixel = sct.grab(monitor).pixel(0, 0)
            if is_red(pixel):
                subprocess.Popen(["afplay", "doom.wav"])
                print("Playing BFG now!")

from pynput import mouse
listener = mouse.Listener(on_click=on_click)
listener.start()


while True:
    time.sleep(0.05)
