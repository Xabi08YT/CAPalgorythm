import webview as pwv
import server as srv
from requests import get
from threading import Thread
from CoreProxy import *
from shutil import rmtree
from os import mkdir, path, getcwd


def shutdown():
    try:
        CoreLibs.utils.unloadDB()
    except Exception:
        pass
    CoreLibs.utils.stop()
    get("http://127.0.0.1:5000/shutdown")
    rmtree(path.join(getcwd(),"tmp"))


mkdir(path.join(getcwd(),"tmp"))


CoreLibs.utils.init()
CoreLibs.issueHandler.init()

cfg, DB = CoreLibs.utils.getVars()
srv.init(cfg,DB)


window = pwv.create_window(title = "Logiciel de gestion CAPS (local)",url="http://127.0.0.1:5000/", confirm_close=True)
window.events.closed += shutdown


t1 = Thread(target=srv.srv.run)
t1.start()
pwv.start(debug=True)
