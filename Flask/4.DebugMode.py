from flask import Flask
import logging
maximum_readbility_format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s'
logging.basicConfig(level=logging.ERROR,filename="logging.txt",format=maximum_readbility_format)
logger=logging.getLogger(__name__)
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
    try:
        return f"100th{name[100]}" #every letter will not have 100th letter
    except IndexError as ex:
        logger.error(str(ex))
        raise
if __name__=="__main__":
    app.run(debug=True)
