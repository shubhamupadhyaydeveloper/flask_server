from server import app,db
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

@app.route("/api/save",methods=["POST"])
def register_friend():
    data = request.json
    name = data.get('name')
    gender = data.get('gender')
    age = data.get('age')
    image_url = ''

    if gender == 'male':
        image_url = f'https://avatar.iran.liara.run/public/boy?username={name}'
    elif gender == 'female':
        image_url = f'https://avatar.iran.liara.run/public/girl?username={name}'
        
    try:
      new_friend = Friend(name=name,gender=gender,age=age,image_url=image_url)
      db.session.add(new_friend)
      db.session.commit()

      return jsonify({"message" : "user created successul","friend" : new_friend.to_json()}),201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error" : str(e)}),500