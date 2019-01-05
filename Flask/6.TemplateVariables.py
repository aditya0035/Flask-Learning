from flask import Flask,render_template
app=Flask(__name__)

"""
@app.route("/")
def BasicTemplate():
    some_variable="Jose"
    return render_template("basic6.html",my_variable=some_variable)
"""
@app.route("/")
def BasicTemplate():
    name="Jose"
    letter=list(name)
    return render_template("basic6.html",name=name,letter=letter)

if __name__=="__main__":
    app.run(debug=True)
