from flask import Flask, request, jsonify
from panda import addRate

app = Flask(__name__)
z=[{"name":"python"}]
@app.route("/", methods = ["get"])
def print():
    return jsonify({"languages":z})
@app.route("/s/add", methods = ["POST"])

def addRating():
    eventId = request.form["eventId"]
    userId = request.form["userId"]
    rating = request.form["rating"]
    status = addRate(userId, eventId, rating)

    return status


# Running the server in localhost:5000
if __name__ == "__main__":
    app.run(debug=True, port=8000)