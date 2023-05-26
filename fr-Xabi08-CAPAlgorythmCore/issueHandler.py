from github import *
from psutil import *
import platform
from contextlib import redirect_stdout
from os import getcwd
CoreLibs = __import__("fr-Xabi08-CAPAlgorythmCore", globals(), locals(), ["utils"],0)


def getLogContent():
    with open(file='lastestlog.txt', mode = 'r') as lastestlog:
        content = lastestlog.readlines()
        lastestlog.close()
    return content


def get_token():
    try:
        with open(file="token.bin", mode="rb") as tokenfile:
            token = tokenfile.read()
            tokenfile.close()
        token = token.decode("utf-8")
        return token
    except FileNotFoundError:
        return "Err"


def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


def getSystemInfos():
    with open("lastestlog.txt", "a+") as f:
        with redirect_stdout(f):
            print("##########################################")
            print("##     Detailed system informations     ##")
            print("##########################################")
            
            print("="*40, "System Information", "="*40)
            uname = platform.uname()
            print(f"System: {uname.system}")
            print(f"Node Name: {uname.node}")
            print(f"Release: {uname.release}")
            print(f"Version: {uname.version}")
            print(f"Machine: {uname.machine}")
            print(f"Processor: {uname.processor}")

            # let's print CPU information
            print("="*40, "CPU Info", "="*40)
            # number of cores
            print("Physical cores:", cpu_count(logical=False))
            print("Total cores:", cpu_count(logical=True))
            # CPU frequencies
            cpufreq = cpu_freq()
            print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
            print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
            print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
            # CPU usage
            print("CPU Usage Per Core:")
            for i, percentage in enumerate(cpu_percent(percpu=True, interval=1)):
                print(f"Core {i}: {percentage}%")
            print(f"Total CPU Usage: {cpu_percent()}%")

            # Memory Information
            print("="*40, "Memory Information", "="*40)
            # get the memory details
            svmem = virtual_memory()
            print(f"Total: {get_size(svmem.total)}")
            print(f"Available: {get_size(svmem.available)}")
            print(f"Used: {get_size(svmem.used)}")
            print(f"Percentage: {svmem.percent}%")
            print("="*20, "SWAP", "="*20)
            # get the swap memory details (if exists)
            swap = swap_memory()
            print(f"Total: {get_size(swap.total)}")
            print(f"Free: {get_size(swap.free)}")
            print(f"Used: {get_size(swap.used)}")
            print(f"Percentage: {swap.percent}%")

            print("="*40, "Disk Information", "="*40)
            print("Partitions and Usage:")
            # get all disk partitions
            partitions = disk_partitions()
            for partition in partitions:
                print(f"=== Device: {partition.device} ===")
                print(f"  Mountpoint: {partition.mountpoint}")
                print(f"  File system type: {partition.fstype}")
                try:
                    partition_usage = disk_usage(partition.mountpoint)
                except PermissionError:
                    # this can be catched due to the disk that
                    # isn't ready
                    continue
                print(f"  Total Size: {get_size(partition_usage.total)}")
                print(f"  Used: {get_size(partition_usage.used)}")
                print(f"  Free: {get_size(partition_usage.free)}")
                print(f"  Percentage: {partition_usage.percent}%")
                # get IO statistics since boot
                disk_io = disk_io_counters()
            print(f"Total read: {get_size(disk_io.read_bytes)}")
            print(f"Total write: {get_size(disk_io.write_bytes)}")

            print(f"Current Exec path: {getcwd()}")
    return


def issueTemplate(title, body, labels = None):
    with open("lastestlog.txt", "a+") as f:
        with redirect_stdout(f):
            getSystemInfos()
            body = body + "\n \n ============LOGS============ \n \n ```" + CoreLibs.utils.transformToText(getLogContent())+" ```"
            if labels is not None:
                try:
                    repo.create_issue(title=title, body=body, labels=labels)
                except Exception as e:
                    print(e)
                    f.close()
                    return False
                f.close()
                return True
            try:
                repo.create_issue(title, body)
            except Exception as e:
                print(e)
                f.close()
                return False
        f.close()
    return False


def getLabel(name):
    label = repo.get_label(name)
    return label


def getLabels():
    global labels
    labels = repo.get_labels()
    return labels


def init():
    global g, repo
    try:
        out = get_token()
        if out == "Err":
            raise Exception("Token.bin missing or empty.")
        g = Github()
        repo = g.get_repo("Xabi08YT/CAPalgorythm")
    except Exception as e:
        return "Error","Impossible de se connecter à github. Veuillez demander au distributeur \ndu programme de générer un nouveau jeton d'accès et de le mettre dans le fichier token.bin"
    return None, None