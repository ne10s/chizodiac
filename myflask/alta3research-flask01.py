#!/usr/bin/python3

from flask import Flask
from flask import redirect
from flask import request
from flask import render_template
from flask import jsonify
from flask import url_for
from flask import session
app = Flask(__name__)
app.secret_key = "secret"

html= """<style>
body {
  background-color: black;
  text-align: center;
  color: white;
  font-family: Arial, Helvetica, sans-serif;
}
</style>
</head>
<body>

<h1>TRIVIA TIME</h1>
<p>What is the meaning of life, the universe, and everything?</p>
<ul>
    <li>Happiness</li>
    <li>Relationship</li>
    <li>Suffering</li>
    <li>Meaningless</li>
    <li>Meaningful</li>
    <li>All and more!</li>
</ul>
<img src="https://stevetobak.com/wp-content/uploads/2021/02/dont-panic.png" alt="Avatar" style="width:200px">

    <form action = "/login" method = "POST">
        <p><input type = "text" name = "nm"></p>
        <p><input type = "submit" value = "submit"></p>
    </form>

</body>
</html>"""
data = {"name": "Life"}
     
#@app.route("/correct")
#def success():
 #   return f"That is correct!"

@app.route("/")
def start():
    return html

@app.route("/login", methods = ["POST"])
def login():
        if request.method=='POST':
            answer = request.json
            if answer:
                solution= answer["solution"]
                if solution=="All and more!":
                    return jsonify(data)     

        else:
            return redirect("/")
@app.route("/protected/<name>")
def ses(name):
    session["username"] = name
    if session["username"] == "Neten":
        return "Info noted"
    else:
        return "Oh I don't know you"
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
