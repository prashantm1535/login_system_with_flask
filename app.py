from flask import Flask, request, render_template, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "our secret_key"


# Configure SQL Alchemy then it creates "instance" folder to application directory
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_DATABASE_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# Database model ~ Single row in our db
class User(db.Model):
    # Class Variables
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def set_password(self, password):
        return check_password_hash(self.password_hash, password)


# Route for home page
@app.route("/")
def home():
    if "username" in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')


# Route for login page
@app.route('/login', methods=["POST"])
def login():
    # Collect info from the form, Check if its in the db/login, otherwise show the home page
    username = request.form["username"]
    password = request.form["password"]
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        session['username'] = username
    else:
        return render_template('index.html')


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="127.0.0.1", port=5656, debug=True)
