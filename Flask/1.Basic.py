from flask import Flask
app=Flask(__name__)

@app.route("/")
def Index():
    return "<h1>Hello Puppy! </h>"

if __name__=="__main__":
    app.run()
