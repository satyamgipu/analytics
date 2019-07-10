from flask import Flask,jsonify,request
import pandas as pd
app = Flask(__name__)
language=[{"name":"python"},{"name":"ruby"}]

@app.route("/",methods=['GET'])
def test():
   return jsonify({"message":"it works"})

@app.route("/lang",methods=["GET"])
def lang():
    return jsonify({"languages":language})

@app.route("/lang/<string:name>",methods=["GET"])
def returnsp(name):
    lang=[languages for languages in language if languages["name"]==name]
    return jsonify({"languages":lang[0]})

@app.route("/lang",methods=["POST"])
def insert():
    new_one = {"name":request.json["name"],"age":request.json["age"]}
    language.append(new_one)
    return jsonify({"language":language})

@app.route("/lang/<string:name>",methods=["PUT"])
def edit(name):
    edit_one=[languages for languages in language if languages["name"]==name ]
    edit_one[0]["name"]=request.json["name"]
    return jsonify({"language":edit_one[0]})


@app.route("/lang/<string:name>",methods=["delete"])
def remove(name):
    remove_ele = [languages for languages in language if languages["name"]==name ]
    language.remove(remove_ele[0])
    return jsonify({"language":language})


if __name__=='__main__':
    app.run(debug=True,port=8010)

