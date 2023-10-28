from flask import *
from os import getpid, system
from CoreProxy import *


toDelete = ["mode","surname","name","group","subjects","freetime","="]
cfgSRV = {}
DBSRV = None


srv = Flask("Serveur local CAPS")


def shutdown_server():
    system("taskkill /f /PID "+str(getpid()))
    
    
@srv.get('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

@srv.get("/")
def index():
    return render_template('index.html')


@srv.post("/")
def index_post():
    try:
        datas = request.get_data().decode('utf-8')
        for i in toDelete:
            datas = datas.replace(i,"")
        datas = datas.split("&")
        print(datas)
        CoreLibs.backendEntry.modeSplit(datas)
        return "OK ! ",200
    except Exception as e:
        print(datas)
        print(f"[STDERR] > {e}")
        with open("exception.txt", mode='w+') as exceptionFile:
            exceptionFile.write(str(e))
            exceptionFile.close()
        return "Internal server error", 500
    

@srv.get("/refreshDB")
def refresh():
    CoreLibs.utils.refreshDB()
    return "Done", 200
    

def init(conf,db):
    global cfgSRV, DBSRV
    cfgSRV = conf
    DBSRV = db
    return