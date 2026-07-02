from flask import Flask, request,redirect,url_for,render_template,session
from dotenv import load_dotenv
import os
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired,Length
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate   
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

class MyForm(FlaskForm):
    name = StringField("name", validators=[DataRequired(),Length(max=100)])
    email = StringField("email", validators=[Length(max=120)])
    submit = SubmitField("Submit")
    
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "history"

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class Users(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120),nullable=False,server_default="")
    history = db.relationship('History', backref='user', lazy=True)
    
    table_args  = (db.UniqueConstraint('email', name='unique_users_email'),)
    
    def __repr__(self):
        return f"User('{self.name}')"

class History(db.Model):
    __table_name__ = "history"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, server_default="")
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    



@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/history",methods=["GET", "POST"])
def history():
    users = Users.query.all()
    return render_template("history.html", users=users)

@app.route("/friends",methods=["GET", "POST"])
def friends():
    name = request.args.get("name", "Friend")
    email = request.args.get("email", "")
    form = MyForm()
    curr_users = Users.query.all()
    
    if form.validate_on_submit():
        name = form.name.data
        email = form.data.get("email", "")  
        user = Users.query.filter_by(name=form.name.data).first()
        if user is None:
            user = Users(name=form.name.data, email=email)
            db.session.add(user)
            db.session.commit() 
            
        return redirect(url_for("friends", name=name))
    return render_template("friends.html", form=form, name=name,email=email, curr_users=curr_users)

@app.route("/add", methods=["GET", "POST"])
def add():
    form = MyForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(name=form.name.data).first()
        if user is None:
            user = Users(name=form.name.data, email=form.data.get("email", ""))
            db.session.add(user)
            db.session.commit()

            return redirect(url_for("add", name=form.name.data, email=form.data.get("email", "")))
        curr_users = Users.query.all()
        return render_template("friends.html", form=form, curr_users=curr_users)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    