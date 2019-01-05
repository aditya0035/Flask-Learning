from flask import Flask
app=Flask(__name__)

@app.route("/")
def Index():#will be called as 127.0.0.1:5000/
    return "<h1>Hello Puppy! </h>"

@app.route("/Information") #will e called as 127.0.0.1:5000/Information
def info():
    return "<h1>Puppies are cute</h1>"

if __name__=="__main__":
    app.run()
