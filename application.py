from flask import Flask,render_template,request,redirect,url_for
import csv

app= Flask(__name__)

@app.route("/")
def index():
    file = open("registered.csv","r")
    reader=csv.reader(file)
    students=list(reader)
    return render_template("comment.html",students=students)

@app.route("/register",methods=["POST","GET"])
def register():
    if request.method == "POST":
        if((request.form.get("name")) == ""):
            return("<h4>Are you crazy or what?<br> write something in comment box.</h4>")
        else:

            #for username

            # for commemts
            file = open("registered.csv","a")
            writer = csv.writer(file)
            writer.writerow((request.form.get("username"),request.form.get("name")))
            file.close()

            return redirect(url_for("register"))
    else:



        file = open("registered.csv","r")
        reader=csv.reader(file)
        students=list(reader)
        return render_template("comment.html",students=students)


