host = "0.0.0.0"
port = 6969
##########################################################

from flask import Flask, render_template, request
from turbo_flask import Turbo
from time import ctime, sleep
import threading
from os import system

try:
    from flask_sqlalchemy import SQLAlchemy
except ImportError:
    system("pip install flask-sqlalchemy")
finally:
    from flask_sqlalchemy import SQLAlchemy

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
    ip = request.remote_addr
    return f"<h1>{ip}</h1>"

with app.app_context():
    threading.Thread(target=update_time).start()

def connect():
    sleep(2)
    print('\n')
    ngrok.kill()
    ngrok.set_auth_token("26cbY7RXyNn41SZPnYH4FRjM5gq_2k9UsLbmK9uzNHnCUQGtm")
    u = ngrok.connect(port,bind_tls=True)
    p = ngrok.get_tunnels()
    print(u)

threading.Thread(target=connect).start()

#this is a just modification to view changes

if __name__ == "__main__":
    app.run(host=host, port=port, debug=True, threaded=True, use_reloader=False)
