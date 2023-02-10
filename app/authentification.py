from flask import Flask,render_template,request,redirect,url_for, flash
from .models import User,db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user,login_required,current_user
import bcrypt

def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        e_mail = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=e_mail).first()
        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('login'))
        login_user(user, remember=True)
        return redirect(url_for('profil'))
def signup():
    if request.method == 'GET':
        return render_template('registres.html')
    else:
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password') 
        password_confirm = request.form.get('password_confirm')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email address already exists')
            return redirect(url_for('signup'))

        if password != password_confirm:
            flash('Passwords do not match!')
            return redirect(url_for('signup'))

        hashed_password = generate_password_hash(password)
        new_user = User(first_name=first_name, last_name=last_name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('User has been created')
        return redirect(url_for('login'))

def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('index'))

def index():
    return render_template('index.html',current_user=current_user)

def profil():
    return render_template('index.html', name = current_user.first_name)