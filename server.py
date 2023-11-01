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
    if len(request.cookies) == 0:
        return redirect("/")
    if request.method == 'GET':
        filename = request.cookies
        datas = CoreLibs.utils.getResults(filename['results'])
        if filename["tutoreid"] != None:
            tutore = CoreLibs.tutore.getTutoreNameByID(int(filename["tutoreid"]))[0]
        else:
            tutore = ("NaN","NaN")
        return render_template("results.html",tutoreID = filename["tutoreid"],tutoreName = tutore[0],tutoreSurname = tutore[1],creneaux = datas["creneaux"], creneauxTXT = datas["creneauxTXT"], matieres = datas["subjects"], data = datas["results"])
    else:
        if cfgSRV["enableRel"]:
            datas = request.get_data()
            datas = datas.decode("utf-8")
            datas = datas.replace("tuteurid=","").replace("tutoreid=","").replace("subject=","").replace("time=","").replace("lessons=","")
            datas = datas.split("&")
            try:
                CoreLibs.relations.addRelationship(int(datas[1]),int(datas[0]),datas[2],datas[3],int(datas[4]))
                return "OK !",200
            except Exception as e:
                print("[STDERR] > "+str(e))
                return e


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
        results,id = CoreLibs.backendEntry.modeSplit(datas)
        print(results)
        redirectURL = "/results"
        response = make_response(redirect(redirectURL))
        response.set_cookie("results",str(results))
        response.set_cookie("tutoreid",str(id[0][0]))
        return response, 301
    except Exception as e:
        print(datas)
        print(f"[STDERR] > {e}")
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


@srv.get("/help")
def help_page():
    return render_template("help.html",labels = CoreLibs.issueHandler.getLabels())


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


@srv.post("/ticket")
def open_ticket():
    data = request.get_data().decode("utf-8")
    data = data.replace("title=","")
    data = data.replace("body=","")
    data = data.replace("labels=","")
    data = data.split("&")
    gitLabels = CoreLibs.issueHandler.getLabels()
    labels = []
    for i,e in enumerate(data[2].split(",")):
        if e.lower()=="true":
            try:
                labels.append(CoreLibs.issueHandler.getLabel(gitLabels[i]))
            except Exception as e:
                print(e)
                labels.append(gitLabels[i])
    if CoreLibs.issueHandler.issueTemplate(data[0],data[1],labels):
        return "OK !",200
    return "Erruer",500
                
    

def init(conf,db):
    global cfgSRV, DBSRV
    cfgSRV = conf
    DBSRV = db
    return