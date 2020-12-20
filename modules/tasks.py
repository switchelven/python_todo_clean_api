from modules.sqlite_init import db


class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True)
    description = db.Column(db.String(10000), unique=True)

    def __init__(self, name, description=""):
        self.name = name
        self.description = description

    def __repr__(self):
        return '<Task %r>' % self.username
