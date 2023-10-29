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
        return 'window.location = "http://www.yoururl.com"'
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


@srv.get("/editor/<table>")
def editor(table):
    MainDB = CoreLibs.utils.MainDB
    cursor = MainDB.cursor()
    sqlrequest = "SELECT * FROM '"+table+"'"
    cursor.execute(sqlrequest)
    data = cursor.fetchall()
    file = table+"Editor.html"
    return render_template(file,data=data)


@srv.post("/modifyDB")
def modifyDB():
    rq = request.get_data()
    updaterq = CoreLibs.utils.createModifyRequest(rq)
    MainDB = CoreLibs.utils.MainDB
    print(updaterq)
    cursor = MainDB.cursor()
    cursor.execute(updaterq)
    MainDB.commit()
    return "Received"
    

def init(conf,db):
    global cfgSRV, DBSRV
    cfgSRV = conf
    DBSRV = db
    return