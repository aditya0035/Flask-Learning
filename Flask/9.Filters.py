from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
def Index():
    names_list=["aditya","jose","jack","jim"]
    return render_template("home9.html",names_list=names_list)

if __name__=="__main__":
    app.run(debug=True)
