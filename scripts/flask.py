__author__ = 'HP'


from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('Navbar.html')

if __name__ == "__main__":
    app.run(debug=True)


@app.route("/Login")
def signup():
    return render_template('Login.html')

if __name__ == "__signup__":
    app.run(debug=True)
