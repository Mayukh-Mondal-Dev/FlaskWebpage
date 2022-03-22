host = "0.0.0.0"
port = 6969

##########################################################

from flask import Flask, render_template, request
from turbo_flask import Turbo
from time import ctime, time, sleep
import threading

app = Flask(__name__)
turbo = Turbo(app)

@app.route("/")
def home():

    return render_template("home.html", time_update=ctime())


def update_time():
    while True:
        sleep(1)
        if turbo.clients:
            turbo.push(turbo.update(ctime(), target="time"))

@app.route('/home', methods=["GET"])
def home_page():
    a = ctime()
    ip = request.remote_addr
    return f"<h1>{ip}</h1>"

@app.before_first_request
def before_first_request():
    threading.Thread(target=update_time).start()

app.run(host,port,debug=True,threaded=True)