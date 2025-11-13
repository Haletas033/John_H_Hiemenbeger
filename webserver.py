from threading import Thread

from flask import Flask

app = Flask('')
@app.route('/')
def home():
    return "0"

def run():
    app.run(host='0.0.0.0', port=8080)

def keepalive():
    t = Thread(target=run)
    t.start()