from flask import *
from os import getpid, system
from CoreProxy import *


toDelete = ["mode","surname","name","group","subjects","freetime","="]


srv = Flask("Serveur local CAPS")


def shutdown_server():
    system("taskkill /f /PID "+str(getpid()))


@srv.errorhandler(404)
def pageNotFound(error):
    return render_template("404.html",error=error)

    
@srv.get('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


@srv.route('/results', methods = ['GET','POST'])
def show_results():
    datas = request.cookies
    print(datas)
    if request.method == 'GET':
        return render_template_string("<h1>Voici vos données {{data}}</h1>",data=datas)
    else:
        return "Hello World !"


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
        redirectURL = "/results"
        response = make_response(redirect(redirectURL))
        response.set_cookie("results",str(results))
        return response, 301
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