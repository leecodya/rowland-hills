from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)
business_name = "Rowland Hills Events"

@app.route("/")
def home():
    return render_template("home.html", name=business_name)

@app.route("/about")
def about():
    return render_template("about.html", name=business_name)

@app.route("/contact")
def contact():
    return "Contact Page"

if __name__ == "__main__":
    app.run(debug=True)