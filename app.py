from flask import Flask, request, render_template, redirect, url_for, session 
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "our secret_key"

# Configure SQL Alchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_DATABASE_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Database model

# Route for home page
@app.route("/")
def home():
    if "username" in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="127.0.0.1", port=5656, debug=True)