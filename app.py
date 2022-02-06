from distutils.log import debug

from tenacity import retry_unless_exception_type
from flask import Flask,jsonify,request

app = Flask(__name__)
tasks=[{
    "Contact" : "754682545",
    "Name":"Rohit",
    "done":"False"

},
{   "Contact" : "789457892",
    "Name":"Rahul",
    "done":"False"
}]


@app.route("/add",methods = ["POST"])
def updatedata():
    task = {
        "Contact":request.json['title'],
        "Name":request.json.get('description',""),
        "done":'False'        
    }
    tasks.append(task)
    return jsonify({
        "message": "task added succesfully"
        })

@app.route("/get")
def getdata():
    return jsonify({
        "data":tasks
    })

@app.route("/")
def greetings():
    return "hello Pranay"

if(__name__ =="__main__"):
    app.run(debug=True)