from flask import Flask, request, jsonify
from models import db, Administrator

#Se instancia nuesta aPP en Flask
app = Flask(__name__)
# print("nombre del archivo",__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///proyect.db"
db.init_app(app) #coneccion a las base de datos al ajecutar app


@app.route("/")
def home():
    return "<h1>Probando flask<h1/>"


@app.route("/create_user", methods=["POST"])
def create_user():
    #===INSTANCIA DE LA TABLA
    user = Administrator()   #crear instancia
 #=== CAPTURA DE DATA   
    data = request.get_json()
    user.rut = data["rut"]
    user.password = data["password"]
    user.name = data["name"]
    user.last_name = data["last_name"]
    user.email = data["email"]

    db.session.add(user)
    db.session.commit()

    return jsonify({
        "msj": "User created",
        "status": "success"
    }), 200

@app.route("/update_user/<int:id>", methods=["PUT"]) #===indicando actualizar por el ID==
def update_user(id):
    user = Administrator.query.get(id)
    if user is not None:
        data = request.get_json()
        user.name = data["name"]

        db.session.commit()

        return jsonify({
        "msj": "User updated",
        "status": "success"
    }), 201
    else:
        return jsonify({
        "msj": "User not found",
        "status": "error"
    }),404

@app.route("/delete_user/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = Administrator.query.get(id)
    if user is not None:
        db.session.delete(user)
        db.session.commit()

        return jsonify({
        "status": "success"
    }), 201
    else:
        return jsonify({
        "msj": "User not found",
        "status": "error"
    }), 404


with app.app_context():
    db.create_all()

if __name__ == "__main__":  
    app.run(host="localhost", port=8080)
