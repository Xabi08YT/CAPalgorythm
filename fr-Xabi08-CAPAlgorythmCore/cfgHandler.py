import json
from os import remove


basicCfg = {"enableLogs": True, "enableFeedback": False, "enableRelDB": False}


def getCfg():
    try:
        with open('cfg.json', mode='r') as cfgFile:
            cfg = json.load(cfgFile)
            cfgFile.close()
    except FileNotFoundError:
        with open('cfg.json', mode='w+') as cfgFile:
            json.dump(basicCfg,cfgFile)
            cfg = basicCfg
            cfgFile.close()
    return cfg


def resetCfg():
    try:
        remove("cfg.json")
    except FileNotFoundError:
        pass
    return getCfg()