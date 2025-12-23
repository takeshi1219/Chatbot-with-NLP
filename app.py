import os
import time

# Compatibility fix: time.clock was removed in Python 3.8+
if not hasattr(time, 'clock'):
    time.clock = time.perf_counter

from chatbot import CB
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return redirect("/chatbot")

@app.route("/chatbot")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(CB.get_response(userText))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    app.run(host="0.0.0.0", port=port, debug=debug, use_reloader=False)