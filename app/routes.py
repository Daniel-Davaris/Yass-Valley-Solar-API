from app import app, db
from app.models import User
from flask import request, render_template, flash, redirect, url_for
from flask_login import current_user, logout_user, login_user
from app.forms import LoginForm


@app.route('/', methods=["GET", 'POST'])
def dashboard():
    data = None
    if request.method == "POST":
        json = request.get_json()
        # CALCULATION ALGORITHM
    else:
        if current_user.is_anonymous:
            return redirect(url_for('login'))
        return render_template('dashboard.html', data=data)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page:
            next_page = url_for('dashboard')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/inventory', methods=["GET", 'POST'])
def inventory():
    data = None
    if request.method == "POST":
        json = request.get_json()
        # CALCULATION ALGORITHM
    else:
        return render_template('inventory.html', data=data)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))