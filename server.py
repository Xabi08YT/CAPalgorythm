from flask import *
from os import getpid, system

srv = Flask("Serveur local CAPS")
from flask import request
def shutdown_server():
    system("taskkill /f /PID "+str(getpid()))
    
    
@srv.get('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

@srv.route("/")
def index():
    return render_template('index.html')


