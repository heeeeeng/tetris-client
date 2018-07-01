
from pynput import keyboard
from pynput.keyboard import Key

def on_press(key):
    if key == Key.esc:
        keyboard.Listener.stop(None)
    try:
        print("key {0} pressed".format(key.char))
    except AttributeError:
        print("special key {0} pressed".format(key))


if __name__ == "__main__":
    with keyboard.Listener(
        on_press=on_press 
    ) as listener:
        listener.join()

    print("lalalala")


