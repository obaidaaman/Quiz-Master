from app import create_app, db, login_manager
from flask import render_template, redirect, flash, url_for
from app.models import User, Subject 

from app.forms import RegisterForm , LoginForm

from flask_login import login_user, login_required, logout_user
app = create_app()

@login_manager.user_loader
def load_user(user_id):
     return User.query.get(user_id)

@app.cli.command('db-create')
def create_db():
        db.create_all()
        print("Database created!")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
         user = User.query.filter_by(username = form.username.data).first()
         if user and user.check_password(form.password.data):
              login_user(user)
              flash('Login Successfull', category= "success")
              return redirect(url_for('dashboard'))
         else:
              flash("Authentication failed!", category="error")
         
    return render_template("login.html", form = form)

@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
         user = User(
              username = form.username.data,
              fullName = form.fullName.data,
              qualification = form.qualification.data,
              dob = form.dob.data)
         
         user.set_password(form.password.data)
         db.session.add(user)
         db.session.commit()
         flash('Registration completed', category= "success")
         return redirect(url_for('login'))
    return render_template("register.html", form = form)


@app.route("/dashboard", methods = ['GET', 'POST'])
@login_required
def dashboard():
    return render_template("dashboard.html")


@app.route("/logout")
@login_required
def logout():
     logout_user()
     flash('Logout Successfull', category= "success")
     return redirect(url_for('login'))
