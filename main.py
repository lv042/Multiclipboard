import time
from typing import NamedTuple
import keyboard
import win32gui, win32con


Version = "0.1"

Logo = """ __  __ _   _ _   _____ ___       ____ _     ___ ____  ____   ___    _    ____  ____  
|  \/  | | | | | |_   _|_ _|     / ___| |   |_ _|  _ \| __ ) / _ \  / \  |  _ \|  _ \ 
| |\/| | | | | |   | |  | |_____| |   | |    | || |_) |  _ \| | | |/ _ \ | |_) | | | |
| |  | | |_| | |___| |  | |_____| |___| |___ | ||  __/| |_) | |_| / ___ \|  _ <| |_| |
|_|  |_|\___/|_____|_| |___|     \____|_____|___|_|   |____/ \___/_/   \_\_| \_\____/ 
                                                                                      
                                                                                                 
"""

available_commands = "[0] Add a shorcut\n" \
                      "[1] List all shorcuts\n" \
                      "[2] Delete a shortcut\n" \
                      "[3] Minimise\n"            \
                        "[4] Exit"

shortcuts_ls = []

class shortcut(NamedTuple):
    shortcut: str
    text: str
    rem: object
window = None
open = True


def startup():
    global window
    window = win32gui.GetForegroundWindow()
    keyboard.add_hotkey(f'strg+m', lambda: show_console())
    print(Logo)
    print(f"Welcome to Multiclipboard {Version}", end= "\n\n")

def write_text(text):
    keyboard.write(text)

def add_shortcut():
    time.sleep(0.5)
    print("Press the first key of the shortcut you want to add\n")
    input1 = keyboard.read_key()
    time.sleep(0.5)
    print("add the second key you want to add\n")
    input2 = keyboard.read_key()
    time.sleep(0.5)
    print(f"Your shortcut is {input1} + {input2}\n")
    print("Enter the text the shortcut should store\n")
    text = input()

    remove = keyboard.add_hotkey(f'{input1}+{input2}', lambda: write_text(text))

    shortcut_obj = shortcut(shortcut=f"{input1} + {input2}", text=text, rem=remove)
    shortcuts_ls.append(shortcut_obj)
    return

def remove_hotkey():
    print("Enter a number:")
    list_all_shortcuts()
    number = int(input())
    keyboard.remove_hotkey(shortcuts_ls[number].rem)
    shortcuts_ls.remove(shortcuts_ls[number])



    print("Hotkey deleted\n")


def enter_text(text):
    keyboard.write(text)

def list_all_shortcuts():
    if len(shortcuts_ls ) == 0:
        print("There are no saved shortcuts\n")
        return
    for i in range(0, len(shortcuts_ls)):
        print(f"[{i}] {shortcuts_ls[i].text} | {shortcuts_ls[i].shortcut}")
    print("")

def hide_console():
    global open
    open = False
    print("This windows minimises in 5 seconds. To open up the window again press Strg + M\n")
    time.sleep(5)

    win32gui.ShowWindow(window, win32con.SW_HIDE)

def show_console():
    global open
    open = True
    if not open:
        hide_console()
    win32gui.ShowWindow(window, win32con.SW_SHOW)

def menu(status):
    match status:
        case 0:
            add_shortcut()
        case 1:
            list_all_shortcuts()
        case 2:
            remove_hotkey()
        case 3:
            hide_console()
        case 4:
            exit()

startup()
while True:
    try:
        print("Enter a number:")
        print(available_commands+"\n")
        number = None
        while not isinstance(number, int):
                number = int(input())
        menu(number)
    except Exception as e:
        print(e)










