from flask import Flask, request, jsonify
from models import db, Student, Apfinancial, Apacademic, Administrator, Grade, Course, Status, Roll
from flask_migrate import Migrate

#Se instancia nuesta aPP en Flask
app = Flask(__name__)
# print("nombre del archivo",__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///proyect.db"
db.init_app(app) #coneccion a las base de datos al ajecutar app
migrate = Migrate(app, db)

@app.route("/")
def home():
    return "<h1>Probando flask<h1/>"


@app.route("/create_account", methods=["POST"])
def create_account():
    #===INSTANCIA DE LA TABLA
    user = Administrator()   #crear instancia
    #=== CAPTURA DE DATA
    if user is not None:   
        data = request.get_json()
        user.rut = data["rut"]
        user.password = data["password"]
        user.email_student = data["email_student"]


        db.session.add(user)
        db.session.commit()

        return jsonify({
            "msj": "Student created",
            "status": "success"
        }), 200
    else:
        return jsonify({
            'msj': 'Student not created',
            'status': "Error"
        }), 404

@app.route("/update_student", methods=["POST"]) #llenar datos de estudiante
def update_student():
    user = Student()
    if user is not None:
        data = request.get_json()
        user.password = data["password"]
        user.name = data["name"]
        user.last_name = data["last_name"]
        user.gender = data["gender"]
        user.birthday = data["birthday"]
        user.address = data["address"]
        user.health_system = data["health_system"]
        user.observation = data["observation"]

        db.session.commit()

        return jsonify({
        "msj": "Student updated",
        "status": "success"
    }), 201
    else:
        return jsonify({
        "msj": "not found",
        "status": "error"
    }), 404

@app.route("/edit_student/<int:id>", methods=["PUT"]) #===indicando actualizar por el ID==
def edit_student(id):
    user = Student.query.get(id)
    if user is not None:
        data = request.get_json()
        #user.rut_student = data["rut_student"]
        user.password = data["password"]
        user.name = data["name"]
        user.last_name = data["last_name"]
        user.gender = data["gender"]
        user.birthday = data["birthday"]
        user.address = data["address"]
        #user.email_student = data["email_student"]
        user.health_system = data["health_system"]
        user.observation = data["observation"]
        #user.course = data["course"]

        db.session.commit()

        return jsonify({
        "msj": "Student updated",
        "status": "success"
    }), 201
    else:
        return jsonify({
        "msj": "Student not found",
        "status": "error"
    }), 404

@app.route("/update_financial", methods=["POST"])
def update_financial():
    user = Apfinancial()
    if user is not None:
        data = request.get_json()
        user.rut_financial = data["rut_financial"]
        user.name = data["name"]
        user.last_name = data["last_name"]
        user.contact_number = data["contact_number"]
        user.address = data["address"]
        user.email_financial = data["email_student"]

        db.session.commit()

        return jsonify({
        "msj": "Financial updated",
        "status": "success"
    }), 201
    else:
        return jsonify({
        "msj": "Financial not found",
        "status": "error"
    }),404

@app.route("/edit_financial/<int:id>", methods=["PUT"]) #===indicando actualizar por el ID==
def edit_financial(id):
    user = Apfinancial.query.get(id)
    if user is not None:
        data = request.get_json()
        user.rut_financial = data["rut_financial"]
        user.name = data["name"]
        user.last_name = data["last_name"]
        user.contact_number = data["contact_number"]
        user.address = data["address"]
        user.email_financial = data["email_student"]

        db.session.commit()

        return jsonify({
        "msj": "Financial updated",
        "status": "success"
    }), 201
    else:
        return jsonify({
        "msj": "Financial not found",
        "status": "error"
    }),404

@app.route("/update_academic", methods=["POST"])
def update_academic():
    user = Apacademic()
    if user is not None:
        data = request.get_json()
        user.rut_financial = data["rut_financial"]
        user.name = data["name"]
        user.last_name = data["last_name"]
        user.contact_number = data["contact_number"]
        user.address = data["address"]
        user.email_financial = data["email_student"]

        db.session.commit()

        return jsonify({
        "msj": "Academic updated",
        "status": "success"
    }), 201
    else:
        return jsonify({
        "msj": "Academic not found",
        "status": "error"
    }),404

@app.route("/edit_academic/<int:id>", methods=["PUT"]) #===indicando actualizar por el ID==
def edit_academic(id):
    user = Apacademic.query.get(id)
    if user is not None:
        data = request.get_json()
        user.rut_financial = data["rut_financial"]
        user.name = data["name"]
        user.last_name = data["last_name"]
        user.contact_number = data["contact_number"]
        user.address = data["address"]
        user.email_financial = data["email_student"]

        db.session.commit()

        return jsonify({
        "msj": "Academic updated",
        "status": "success"
    }), 201
    else:
        return jsonify({
        "msj": "Academic not found",
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

######################## GET POINT ###############################
@app.route('/students')
def list_student():
    students = Student.query.with_entities(Student.rut_student, Student.name, Student.last_name).all()
    result_students = [{"rut": rut, "name": nombre, "last_name": apellido} for rut, nombre, apellido in students]
    return jsonify(result_students)

@app.route('/courses')
def list_course():
    courses = Course.query.with_entities(Course.course).all()
    result_courses = [{"course": course} for course in courses]
    return jsonify(result_courses)

if __name__ == "__main__":  
    app.run(host="localhost", port=8080)
