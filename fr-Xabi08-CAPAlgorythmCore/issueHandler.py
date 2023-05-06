from github import *


def getLogContent():
    with open(file='lastestlog.txt', mode = 'r') as lastestlog:
        content = lastestlog.readlines()
        lastestlog.close()
    return content


def get_token():
    with open(file="token.bin", mode="rb") as tokenfile:
        token = tokenfile.read()
        tokenfile.close()
    return token


def issueTemplate(title, body, labels = None):
    body = body + "\n ============LOGS============ \n" + getLogContent()
    if labels is not None:
        try:
            repo.create_issue(title=title, body=body, labels=labels)
        except Exception as e:
            print(e)
            return 
        return
    try:
        repo.create_issue(title, body)
    except Exception as e:
        print(e)
        return 
    return


def getLabel(name):
    label = repo.get_label(name)
    return label


def init():
    global g, repo
    g = Github(get_token())
    repo = g.get_repo("Xabi08YT/CAPalgorythm")
    return