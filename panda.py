import csv
import json
import pandas as pd
from flask import Flask,jsonify,request



app=Flask(__name__)
with open('s.csv', 'a', newline='') as csvfile:
    fieldnames = ['name', 'age','gender']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
 #   writer.writeheader()
    writer.writerow({'name': 'satyam', 'age': '19','gender':'male'})
    csvfile.close()
z=[{"name":"satyam","age":"22","gender":"male"}]

@app.route("/new",methods=["POST"])
def insert():
   newone={"name":request.json["name"],"age":request.json["age"],"gender":request.json["gender"]}

   newone=json.dumps(newone)
   newone =json.loads(newone)
   with open ('s.csv',"a",newline='')as csvfile:
       #fieldnames = ["name","age","gender"]
       writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
       writer.writerow(newone)
       csvfile.close()

   z.append(newone)
   return jsonify(z)


@app.route("/delete",methods=["POST"])
def delete():
  del_name = request.form["name"]

  data = pd.read_csv("s.csv", index_col="name")
  data.drop([del_name],inplace=True)
  data.to_csv("s.csv")

  return jsonify(z)


@app.route("/",methods=["GET"])
def data():
    data = pd.read_csv("s.csv")
    return jsonify(data)

z=[{"key":"value"}]
y=[{}]
@app.route("/uploads",methods=["POST"])
def uploads():

        file = request.files["file"]
        name=file.filename
        if file :
            path="/home/tatras/PycharmProjects/upload/"+name
            file.save(path)
            print(path)
            return jsonify(z)
        else :

            return jsonify(y)


if __name__=="__main__":
    app.run(debug=True,port=8010)
