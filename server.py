from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

USERNAME = "admin"
PASSWORD = "password"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == USERNAME and password == PASSWORD:
            return redirect(url_for("Welcome"))
        else:
            return render_template("login.html",
                                   error="Invalid usernae or password")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)