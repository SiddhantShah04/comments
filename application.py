from flask import Flask,render_template,request,redirect,url_for
import csv

app= Flask(__name__)

@app.route("/")
def index():
    file = open("registered.csv","r")
    reader=csv.reader(file)
    students=list(reader)
    return render_template("Chat.html",students=students)

@app.route("/register",methods=["POST","GET"])
def register():
    if request.method == "POST":

        file = open("registered.csv","a")
        writer = csv.writer(file)
        writer.writerow((request.form.get("name")))
        file.close()

        file = open("registered.csv","r")
        reader=csv.reader(file)
        students=list(reader)
        return redirect(url_for("register"))
    else:
        file = open("registered.csv","r")
        reader=csv.reader(file)
        students=list(reader)
        return render_template("Chat.html",students=students)


