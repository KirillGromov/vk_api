from flask import Blueprint, render_template, redirect, url_for, session
from .forms import RegForm, LogForm
from model import *
auth = Blueprint('auth', __name__, template_folder="templates")

@auth.route("/register", methods=['POST', 'GET'])
def register():
    form = RegForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        print('username')

        user_object = User.query.filter_by(username=username).first()
        if user_object:
            
            return redirect(url_for('index'))

        user = User(username = username, password = password)
        db.session.add(user)
        db.session.commit()
        print("good")
        return redirect(url_for('index'))
    
    return render_template("reg.html", form=form)

@auth.route("/login", methods=['POST', 'GET'])
def login():
    form = LogForm()
    username_entered = form.username.data
    password_entered = form.password.data
    token_entered = form.token.data
    if form.validate_on_submit():
        user_object = User.query.filter_by(username=username_entered).first()
        if user_object is None:
            print("Нет такого пользователя")
            return render_template("log.html", form=form)
        elif password_entered != user_object.password:
            print("Неправильный пароль")
            return render_template("log.html", form=form)
        session["log"] = True
        session["username"] = username_entered
        session["token"] = token_entered
        print(session["username"])
        return redirect(url_for('index'))
    return render_template("log.html", form=form)

@auth.route('/logout')
def logout():
    try:
        del session['username']
        del session['log']
        del session['token']
    except:
        pass
    return redirect(url_for('auth.login'))