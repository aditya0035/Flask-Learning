from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def Index():
    return render_template("home13.html")

@app.errorhandler(404)
def page_not_found(e):
    print(e)
    return render_template("404NotFound13.html"),404

if __name__=="__main__":
    app.run(debug=True)
