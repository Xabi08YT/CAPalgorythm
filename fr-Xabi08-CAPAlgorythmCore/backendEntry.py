CoreLibs = __import__("fr-Xabi08-CAPAlgorythmCore", globals(), locals(), ["utils","DBCreator","tuteurs", "relations","feedback", "issueHandler","groupes","cfgHandler","tutore"],0)
from random import randint
from json import dump


def modeSplit(data):
    if data[0] == "Add":
        freetime = CoreLibs.utils.parseDispos(data[5])
        subjects = CoreLibs.utils.parseSubjects(data[4])
        groupid = CoreLibs.groupes.getGroupByName(data[3])[0][0]
        CoreLibs.tuteurs.addTuteur(data[1],data[2],groupid,freetime,subjects)
        return "Successfully added tuteur."
    elif data[0] == "Rem":
        CoreLibs.tuteurs.deleteTuteur(data[1],data[2],CoreLibs.groupes.getGroupByName(data[3])[0][0])
        return "Successfully removed tuteur."
    elif data[0] == "Sea":
        config = CoreLibs.utils.config
        freetime = CoreLibs.utils.parseDispos(data[5],True)
        subjects = CoreLibs.utils.parseSubjects(data[4],True)
        groupLVL = CoreLibs.groupes.groupGetLVL(data[3])[0][0]
        res = CoreLibs.tuteurs.findTuteur(groupLVL,freetime,subjects)
        rdnb = str(randint(0,65265744984616286))
        if config["enableRel"]:
            groupid = CoreLibs.groupes.getGroupByName(data[3])[0][0]
            CoreLibs.tutore.addTutore(data[1],data[2],groupid,CoreLibs.utils.transformToText(freetime).replace("%",""),CoreLibs.utils.transformToText(subjects).replace("%",""))
            tutoreid = CoreLibs.tutore.getTutoreID(data[1],data[2],groupid)
        else:
            tutoreid = None
        with open("tmp/"+rdnb+".json", mode='w+') as f:
            dump(res,f)
            f.close()
        return rdnb, tutoreid