from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Home page"

@app.route("/about")
def about():
    return "About Page"

@app.route("/contact")
def contact():
    return redirect(url_for("about"))

if __name__ == "__main__":
    app.run(debug=True)