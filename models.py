from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User (db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200), nullable = False)
    password = db.Column(db.String(200), nullable = False)
    username = db.Column(db.String(200), nullable = False)

    def to_dic(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "pasword" : self.password,
            "username" : self.username
        }