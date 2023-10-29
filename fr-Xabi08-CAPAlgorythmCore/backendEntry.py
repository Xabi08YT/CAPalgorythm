CoreLibs = __import__("fr-Xabi08-CAPAlgorythmCore", globals(), locals(), ["utils","DBCreator","tuteurs", "relations","feedback", "issueHandler","groupes","cfgHandler"],0)


def modeSplit(data):
    if data[0] == "Add":
        freetime = CoreLibs.utils.parseDispos(data[5])
        subjects = CoreLibs.utils.parseSubjects(data[4])
        groupid = CoreLibs.groupes.getGroupByName(data[3])[0][0]
        CoreLibs.tuteurs.addTuteur(data[1],data[2],groupid,freetime,subjects)
        return "Successfully added tuteur."
    elif data[0] == "Rem":
        CoreLibs.tuteurs.deleteTuteur(data[1],data[2],CoreLibs.groupes.groupGetLVL(data[3])[0][0])
        return "Successfully removed tuteur."
    elif data[0] == "Sea":
        freetime = CoreLibs.utils.parseDispos(data[5],True)
        subjects = CoreLibs.utils.parseSubjects(data[4],True)
        groupLVL = CoreLibs.groupes.groupGetLVL(data[3])[0][0]
        res = CoreLibs.tuteurs.findTuteur(groupLVL,freetime,subjects)
        return res