import webview as pwv
from server import *
from requests import get
from threading import Thread


def shutdown():
    get("http://127.0.0.1:5000/shutdown")


window = pwv.create_window(title = "Logiciel de gestion CAPS (local)",url="http://127.0.0.1:5000/", confirm_close=True)
window.events.closed += shutdown


t1 = Thread(target=srv.run)
t1.start()
pwv.start()