from flask import Flask,render_template
import re
app=Flask(__name__)

def CustomFilter(item):
    pattern="[^0-9]+"
    return re.findall(pattern,item)[0]
def UpperCase(item):
    return item.upper()

@app.route("/")
def Index():
    names_list=["aditya","jose","jack","jim","Kim09"]
    app.jinja_env.filters["CustomFilter"]=CustomFilter
    return render_template("home10.html",names_list=names_list,UpperCase=UpperCase)

if __name__=="__main__":
    app.run(debug=True)
