CoreLibs = __import__("fr-Xabi08-CAPAlgorythmCore", globals(), locals(), ["utils","DBCreator","tuteurs", "relations","feedback", "issueHandler","groupes","cfgHandler"],0)


def modeSplit(data):
    if data[0] == "Add":
        freetime = CoreLibs.utils.parseDispos(data[5])
        subjects = CoreLibs.utils.parseSubjects(data[4])
        groupid = CoreLibs.groupes.getGroupByName(data[3])[0][0]
        CoreLibs.tuteurs.addTuteur(data[1],data[2],groupid,freetime,subjects)
    elif data[1] == "Rem":
        CoreLibs.tuteurs.deleteTuteur(data[1],data[2],data[3])
    elif data[2] == "Sea":
        freetime = CoreLibs.utils.parseDispos(data[5],True)
        subjects = CoreLibs.utils.parseSubjects(data[4],True)
        groupLVL = CoreLibs.groupes.groupGetLVL(data[3])[0][0]
        print(CoreLibs.tuteurs.findTuteur(groupLVL,freetime,subjects))