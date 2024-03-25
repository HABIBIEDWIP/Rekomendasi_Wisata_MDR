from flask import Flask, render_template, request
from process import preparation, generate_response
from recommendation import rekomendasi
import sys

preparation()

app = Flask("Local Pride")


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/destinasion")
def destination():
    res = rekomendasi()
    return render_template("destination.html", res=res)

@app.route("/rekomendasi_des", methods=["POST"])
def rekomendasi_des():
    data = str(request.form["filter_data"])
    res = rekomendasi(data)
    return render_template("destination.html", res=res)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/get")
def get_bot_respon():
    user_input = str(request.args.get("msg"))
    result = generate_response(user_input)
    return result

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
