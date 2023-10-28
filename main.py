import webview as pwv
import server as srv
from requests import get
from threading import Thread
from CoreProxy import *


def shutdown():
    CoreLibs.utils.unloadDB()
    get("http://127.0.0.1:5000/shutdown")


CoreLibs.utils.init()


cfg, DB = CoreLibs.utils.getVar()
srv.init(cfg,DB)


window = pwv.create_window(title = "Logiciel de gestion CAPS (local)",url="http://127.0.0.1:5000/", confirm_close=True)
window.events.closed += shutdown


t1 = Thread(target=srv.srv.run)
t1.start()
pwv.start(debug=True)