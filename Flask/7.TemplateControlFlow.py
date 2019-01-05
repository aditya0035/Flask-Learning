from flask import render_template,Flask
app=Flask(__name__)
class Puppy:
    def __init__(self,name,age):
        self.name=name
        self.age=age


@app.route("/")
def GetAllPuppies():
    puppy_list=[Puppy("Tommy",5),Puppy("Jacky",8),Puppy("Jack",10),Puppy("Adam",10)]
    return render_template("basic7.html",puppy_list=puppy_list)

if __name__=="__main__":
    app.run(debug=True)
