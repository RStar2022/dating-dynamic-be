from .db import db

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    date = db.Column(db.DateTime, unique=True, nullable=False)
    occupation = db.Column(db.String(64), nullable = False)
    hobby = db.Column(db.String(64), nullable=False)
    gender = db.Column(db.String(64), nullable=False)
    img = db.Column(db.BLOB, nullable=False)

    def __init__(self, name, date, occupation, hobby, gender, img):
        self.name = name
        self.date = date
        self.occupation = occupation
        self.hobby = hobby
        self.gender = gender
        self.img = img
    
    def as_dict(self):
        return {"name":self.name,
                "date":str(self.date),
                "occupation":self.occupation,
                "hobby":self.hobby,
                "gender":self.gender,
                "img":str(self.img)}

        