from app import db

class User(db.Model):
    sl = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.String(50), unique=False, nullable=False)
    name = db.Column(db.String(50), unique=False, nullable=False)
    regno = db.Column(db.String(20), unique=False, nullable=False)
    dpt = db.Column(db.String(120), nullable=False)
    cgpa = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"User('{self.id}', '{self.name}', '{self.regno}', '{self.dpt}', '{self.cgpa}')"