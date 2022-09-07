# UN CODICE PIÙ DINAMICO, SENZA RIPETERE I VARI @app.route

from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)            # __main__ è il nome di app

@app.route('/')
def my_outer_space():
    return render_template("index.html")

@app.route('/<string:page_name>')      # non capisco perché funzioni
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open("Database.txt", mode="a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\nEmail: {email}, Subject: {subject}, Message: {message}")


def write_to_csv(data):
    with open("Database2.csv", newline="", mode="a") as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

# per la pagina contact:
@app.route('/submit_form', methods=['POST', 'GET'])        # GET means the browser wants us to send informations
def submit_form():                                         # POST means the browser wants us to save informations
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("/thankyou.html")   # submitted
        except:
            return "No, non è stato salvato nel database!"
    else:
        return "Qualcosa non va, prova di nuovo!"
