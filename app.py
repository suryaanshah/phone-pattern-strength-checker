
# # 1. to take input, we have a 3x3 pattern the user drags on.
# """
# Psuedo code:
# Event (first click)
#     store the first (x,y) pair in pattern[]
# Event(Drag to another)
#     append this (x,y) to pattern[]
# If pattern[] in common-patterns[]
#     return 1
# else 
#     return 0
# """


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def helloworld():
    name = request.args["name"]
    return render_template("index.html", placeholder=name)
