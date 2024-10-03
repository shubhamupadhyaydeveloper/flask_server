from server import db

class Friend(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    gender = db.Column(db.String(20),nullable=False)
    age = db.Column(db.Integer,nullable=False)
    image_url = db.Column(db.String,nullable=False)
    

    def to_json(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "gender" : self.gender,
            "age" : self.age,
            "imageUrl" : self.image_url
        }