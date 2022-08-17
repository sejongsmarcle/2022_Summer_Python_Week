from flask import url_for, session, Flask, render_template, request, redirect
import sys
import pandas as pd
import plotly
import plotly.graph_objs as go
import plotly.express as px

from numpy import average
app = Flask(__name__)
app.secret_key = "tlzmfltzlrkanjdi"
import database

ID = "smarcle"
PW = "pythonweek"

@app.route("/")
def home():
    if "userID" in session:
        return render_template("home.html", username = session.get("userID"), login = True)
    else:
        return render_template("home.html", login = False)

@app.route("/main")
def main():
    return render_template("main.html")


@app.route("/login" , methods = ["get"])
def login() :
    global ID, PW
    _id_ = request.args.get("loginId")
    _password_ = request.args.get("loginPw")
    
    if _id_ == ID and _password_ == PW :
        session["userID"] = _id_
        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))
    
@app.route("/logout")
def logout():
    session.pop("userID")
    return redirect(url_for("home"))


@app.route("/upload")
def apply():
    return render_template("upload.html")

@app.route("/upload_photo")
def upload_photo():
    date = request.args.get("date")
    title = request.args.get("title")
    feeling = request.args.get("feeling")
    contents = request.args.get("contents")
    
    database.save(date, title, feeling, contents)
    return render_template("upload_photo.html")

@app.route("/upload_done", methods=["POST"])
def upload_done():
    uploaded_files = request.files["file"]
    uploaded_files.save("static/img/{}.jpeg".format(database.now_index()))
    return redirect(url_for("main"))

@app.route("/list")
def list():
    diary_list = database.load_list()
    length = len(diary_list)
    for diary in diary_list:
        print(diary[1])
    return render_template("list.html", diary_list = diary_list, length = length)

@app.route("/diary_info/<int:index>/")
def diary_info(index):
    diary_info = database.load_diary(index)
    date = diary_info["date"]
    title = diary_info["title"]
    feeling = diary_info["feeling"]
    contents = diary_info["contents"]
    
    photo = f"img/{index}.jpeg"
    
    return render_template("diary_info.html", 
        date = date, title = title, feeling = feeling, contents = contents, photo = photo)

@app.route("/emotion")
def emotion():
    avg = database.avg_emotion()
    average = avg
    if avg > 7:
        mood = "good"
    elif avg > 4:
        mood = "soso"
    else:
        mood = "bad"
    return render_template("emotion.html", avg = average, mood = mood)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
