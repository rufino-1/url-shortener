from flask import Flask, render_template
# export FLASK_ENV=development
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html", name="Rufino")

@app.route('/about')
def about():
    return "this is a url shortener!!!**"

