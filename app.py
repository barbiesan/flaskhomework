mport sqlite3
import random
from flask import Flask, session, render_template, request

app = Flask(__name__)
app.secret_key = "$$%^&*()!"


@app.route("/",methods=["POST,"GET"])
def index():
    session["all_inputs"],session["phone_book"]= get_db()
   all_inputs , phone_numbers = get_db()
    return render_template("index.html", all_inputs = session["all_inputs"], phone_numbers = session["phone_numbers"])

@app.route("/add_inputs", method=["post"])
def add_inputs():
    session["phone_numbers"].append()
     return render_template("index.html", all_inputs = session["all_inputs"], phone_numbers = session["phone_numbers"])

@app.route("/remove_inputs", method=["post"])
def remove_inputs():
    checked_boxes=request.form.getlist("check")

    for input in check_boxes:
        if input in session["phone_numbers"]:
        idx =session["phone_numbers"].index(input)
        session["phone_numbers"].pop(idx)
        session.modified=True
return render_template("index.html", all_inputs = session["all_inputs"], phone_numbers = session["phone_numbers"])


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('people_list.db')
        cursor = db.cursor()
        cursor.execute("select * from people")
        all_data = cursos.fetcha11()
        all_data = [str(val[0][1])for val in all_data]

        phone_numbers=  all_data.copy()
        random.shuffle(phone_numbers)

    return all_data, phone_numbers

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run()