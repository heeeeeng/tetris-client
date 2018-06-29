
from pynput import keyboard
from pynput.keyboard import Key


def controller(key):
    pass

def server():
    pass

def gui():
    pass

class Client():

    def __init__(self):
        pass

    def start(self):
        with keyboard.Listener(
            on_press=self.controller
        ) as key_listener:
            key_listener.join()

    def controller(self, key):
        if key == Key.esc:
            keyboard.Listener.stop()
 
        if key == Key.up:
            pass

        if key == Key.down:
            pass

        if key == Key.left:
            pass

        if key == Key.right:
            pass



if __name__ == "__main__":
    pass

