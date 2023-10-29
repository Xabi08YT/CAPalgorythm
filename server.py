from flask import *
from os import getpid, system
from CoreProxy import *


toDelete = ["mode","surname","name","group","subjects","freetime","="]


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
        results = CoreLibs.backendEntry.modeSplit(datas)
        print(results)
        return 'OK !'
    except Exception as e:
        print(datas)
        print(f"[STDERR] > {e}")
        return "Internal server error", 500
    

@srv.get("/refreshDB")
def refresh():
    CoreLibs.utils.refreshDB()
    return "Done", 200


@srv.get("/tuteurEditor")
def tuteurEdit():
    MainDB = CoreLibs.utils.MainDB
    cursor = MainDB.cursor()
    cursor.execute("""SELECT id,name,surname,groupid,freeon,subject FROM 'tuteur'""")
    data = cursor.fetchall()
    return render_template('tuteurEditor.html',data=data)


@srv.post("/modifyDB")
def modifyDB():
    rq = request.get_data()
    updaterq = CoreLibs.utils.createModifyRequest(rq)
    MainDB = CoreLibs.utils.MainDB
    cursor = MainDB.cursor()
    cursor.execute(updaterq)
    MainDB.commit()
    return "Received"
    

def init(conf,db):
    global cfgSRV, DBSRV
    cfgSRV = conf
    DBSRV = db
    return