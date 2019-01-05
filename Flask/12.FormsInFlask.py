from flask import Flask,render_template,request
import re
app=Flask(__name__)

rules=["username must contains lowercase","username must contains uppercase","username must end in a number"]

@app.route("/")
def index():
    return render_template("home12.html",rules=rules)

@app.route("/SaveUserName")
def SaveUserName():
    username=request.args.get("username")
    rulesNotObey=[]
    if not re.search("[a-z]+",username):
        rulesNotObey.append(rules[0])
    if not re.search("[A-Z]+",username):
        rulesNotObey.append(rules[1])
    if not re.search("[0-9]+$",username):
        rulesNotObey.append(rules[2])
    return render_template("report12.html",rulesNotObey=rulesNotObey,len=len)

if __name__=="__main__":
    app.run(debug=True)
