from server import app
from models import Friend
from flask import request,jsonify


@app.route("/")
def home():
    return f"hi welcome to flask server"

@app.route("/api/friends",methods=['GET'])
def get_all_friends():
    friends = Friend.query.all()
    result = [friend.to_json() for friend in friends]
    return jsonify(result)

@app.route("/user/<string:username>",methods=['POST'])
def user_name(username):
    age = request.json['age']
    return f"this is your name {username} and this is your age {age}"

