from pynput.keyboard import Controller, Key, Listener
import argparse
import time

def secs():
    return round(time.time())

Stamp = secs()

# Construct the argument parser
ap = argparse.ArgumentParser()

Timeout = 60*3
Mode = "quiet"
Press = Key.f14
# Add the arguments to the parser
ap.add_argument("-t", "--timeout", required=False, help="Timeout")
ap.add_argument("-m", "--mode", required=False, help="Mode")
args = vars(ap.parse_args())

if args["timeout"] is not None:
    Timeout = int(args["timeout"])

if args["mode"] is not None:
    Mode = args["mode"]

# Calculate the sum
print("Timeout: %ds, mode: %s" % (Timeout, Mode))

keyboard = Controller()

# Type a string
#keyboard.type("echo 'Hello, World!")

# Press and release keys
#keyboard.press("'")
#keyboard.release("'")

# Press a special key
#keyboard.press(Key.enter)
#keyboard.release(Key.enter)

def Nudge():
    keyboard.press(Press)
    keyboard.release(Press)
    if Mode != "quiet":
        print("Wakey-wakers")

#keyboard.press(Key.f14)
#keyboard.release(Key.f14)

def on_press(key):
    if Mode != "quiet":
        print('{0} pressed'.format(key))
    global Stamp
    Stamp = secs()

def on_release(key):
    if Mode != "quiet":
        print('{0} release'.format(key))
    global Stamp
    Stamp = secs()

# Collect events until released
#with Listener(
#        on_press=on_press,
#        on_release=on_release) as listener:
#    listener.join()

# ...or, in a non-blocking fashion:
listener = Listener(
    on_press=on_press,
    on_release=on_release)

listener.start()    

while True:
    if Mode != "quiet":
        print(secs() - Stamp)
    if secs() - Stamp > Timeout:
        Nudge()
    time.sleep(1)
