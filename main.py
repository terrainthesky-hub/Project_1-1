from werkzeug.utils import redirect
from utils.manage_connection import OperationalError, connect
import os


from data_access_layer.employee_dao.employee_imp import EmployeeDAOImp
from data_access_layer.ticket_dao.ticket_imp import TicketDAOImp
from service_access_layer.employee_service_access_layer.employee_sal_imp import EmployeeSALImp
from service_access_layer.ticket_service_access_layer.ticket_sal_imp import TicketSALImp

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app: Flask = Flask(__name__)
CORS(app) # use this to avoid cors errors

employee_dao = EmployeeDAOImp()
employee_service = EmployeeSALImp(employee_dao)

ticket_dao = TicketDAOImp()
ticket_service = TicketSALImp(ticket_dao)

# @app.get("/<name>")
# def get_greeting(name: str):
#     return jsonify({"message": f"Hello {name}"}), 200
#

@app.post("/body")
def sending_http_request_with_body():
    body: dict = request.get_json()
    if correct_id == employee_dao.employee_id_username_password_match(body['username'], body['password']):
        employee_id = employee_dao.employee_id_username_password_match(body['username'], body['password'])
        employee_id = jsonify(employee_id)
        to_send = employee_id
        return redirect("create_and_view_tickets.html", to_send=employee_id), 200
        # return jsonify('employeeId': employee_id), 200

    # return jsonify({"message": "done"}, 200)

# body = request_json()

@app.post("/create_and_view_tickets")
def making_and_seeing_tickets():
    pass




# @app.route('/login', methods=['POST'])
# def login():
#     # if (request.method == 'POST'):
#     username = request.form.get('username')
#     password = request.form.get('password')
#     un = employee_dao.reading_username(username)
#     pw = employee_dao.reading_password(password)
#     if username == un.username and password == pw.password:
#         return redirect("/create_tickets")
#     else:
#         return "<h1>Wrong username or password</h1>"  # if the username or password does not matches
#
#     # return render_template("login.html")

# 
# @app.route("/create_tickets", methods=["POST"])
# def create_ticket_route():
#     pass
# 



# @app.route("/login", methods=["POST"])
# def login():
#
#     credentials = request.get_json()
#     username = credentials["username"]
#     password = credentials["password"]
#     un = employee_dao.reading_username(username)
#     pw = employee_dao.reading_password(password)
#     if username == un.username and password == pw.password:
#         return redirect("http://127.0.0.1:5000/button", code=302)
#     else:
#         return "your credentials are bad!"

# @app.route("/button", methods=['GET', 'POST'])
# def index(form=None):
#     if request.method == 'POST':
#         if request.form.get('action1') == 'Create Ticket':
#             return redirect("http://127.0.0.1:5000/create_ticket")  # do something
#     elif request.method == 'GET':
#         return render_template('index.html', form=form)
#
#     return render_template("index.html")
#
# @app.route("/create_ticket", methods=["POST"])
# def create_ticket_route():
#     pass



app.run()