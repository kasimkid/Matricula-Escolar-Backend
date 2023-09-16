from flask import Flask
from models import db, User

#Se instancia nuesta aPP en Flask
app = Flask(__name__)
# print("nombre del archivo",__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///proyect.db"
db.init_app(app) #coneccion a las base de datos al ajecutar app






if __name__ == "__main__":  
    app.run(host="localhost", port=5000)