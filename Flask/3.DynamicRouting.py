from flask import Flask
app=Flask(__name__)

@app.route("/")
def Index():#will be called as 127.0.0.1:5000/
    return "<h1>Hello Puppy! </h>"

@app.route("/Information") #will e called as 127.0.0.1:5000/Information
def info():
    return "<h1>Puppies are cute</h1>"

@app.route("/puppy/<name>")
def puppy(name):
    return f"<h1>This is page for {name} </h1>"

@app.route("/puppy/upper/<name>")
def upperCasePuppy(name):
    return f"<h1>{name.upper()}</h1>"
if __name__=="__main__":
    app.run()
