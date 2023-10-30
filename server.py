from flask import *
from os import getpid, system
from CoreProxy import *
from time import sleep


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


@srv.get("/settings")
def show_settings():
    return render_template("settings.html",Rel = cfgSRV["enableRel"],Feedback = cfgSRV["enableFeedback"])


@srv.route("/redirect/<link>")
def timedRedirect(link):
    sleep(1)
    return redirect("/"+link)


@srv.post("/cfg/<op>")
def cfgOp(op):
    global cfgSRV
    if op == "refresh":
        cfgSRV = CoreLibs.utils.refreshConfig()
        return "OK !"
    elif op == "reset":
        cfgSRV = CoreLibs.cfgHandler.resetCfg()
        return "OK !"
    elif op == "write":
        data = request.get_data().decode('utf-8')
        data = data.replace("enableRel","")
        data = data.replace("enableFeedback","")
        data = data.replace("=","")
        data = data.split("&")
        if cfgSRV["enableRel"] != data[0] and data[0] == "true":
            CoreLibs.DBCreator.createRelTable()
        if cfgSRV["enableFeedback"] != data[1] and data[1] == "true":
            CoreLibs.DBCreator.createFeedbackTable()
        cfgSRV["enableRel"] = data[0] == "true"
        cfgSRV["enableFeedback"] = data[1] == "true"
        CoreLibs.cfgHandler.writeCfg(cfgSRV)
        return "OK !"
    else:
        return "Error: opcode "+op+" does not exist for url /cfg/",404


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

@srv.post("/DB/reset")
def reset():
    CoreLibs.utils.resetDB()
    return "OK !"
    

def init(conf,db):
    global cfgSRV, DBSRV
    cfgSRV = conf
    DBSRV = db
    return