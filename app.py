from flask import Flask 

app = Flask(name)   

@app.route("/")
def home():
    return "Hello Dosto, This is Sam and another trigger from others Yash!"

if name == "main":
    app.run(host="0.0.0.0", port=5000)
