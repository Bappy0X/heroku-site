from web import db

class comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    text = db.Column(db.String(255))

    def __init__(self, name, text):
        self.name = name
        self.text = text
    
    def __repr__(self):
        return f"{self.id}, {self.name}: {self.text}"