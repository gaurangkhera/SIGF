from Tool import app, db
from Tool.forms import RegistrationForm, LoginForm, ApplicationForm
from Tool.models import User, Application
from flask import render_template, request, url_for, redirect, flash, abort, jsonify, make_response
from flask_login import current_user, login_required, login_user, logout_user
import secrets
from sqlalchemy import desc, asc
import os
import json
from flask import Flask, render_template, request, abort
from datetime import datetime
from werkzeug.security import generate_password_hash


@app.route('/', methods=['GET', 'POST'])
def index():
    # user = User(name1='hello',
    #                 name2='hello',
    #                 name3='hello',
    #                 name4='hello' or '',

    #                 school1='hello',
    #                 school2='hello',
    #                 school3='hello',
    #                 school4='hello' or '',

    #                 email1='admin@studentigf.net',
    #                 emailb='hello',

    #                 phone1=1111111111111111,
    #                 phoneb=12277127,

    #                 am_name = 'hello',
    #                 am_email = 'hello',
    #                 am_phone = 'hello',

    #                 password='password')
    # db.session.add(user)
    # db.session.commit()
    return render_template("index.htm")


@app.route('/about')
def about():
    return render_template('about.htm')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        print(9)
        user = User(name1=form.name1.data,
                    name2=form.name2.data,
                    name3=form.name3.data,
                    name4=form.name4.data or '',

                    school1=form.school1.data,
                    school2=form.school2.data,
                    school3=form.school3.data,
                    school4=form.school4.data or '',

                    email1=form.email1.data,
                    emailb=form.emailb.data,

                    phone1=form.phone1.data,
                    phoneb=form.phoneb.data,

                    am_name=form.am_name.data,
                    am_email=form.am_email.data,
                    am_phone=form.am_phone.data,

                    password=form.password.data)
        print('hey')
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('index'))
    return render_template('register.htm', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error = ''
    if form.validate_on_submit():
        user = User.query.filter_by(email1=form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            next = request.args.get('next')
            if next == None or not next[0] == '/':
                next = url_for('index')
            return redirect(next)
        elif user is not None and user.check_password(form.password.data) == False:
            error = 'Incorrect password.'
        elif user is None:
            error = 'Account not found.'
    return render_template('login.htm', form=form, mess=error)


@app.route('/apply', methods=['GET', 'POST'])
def apply():
    form = ApplicationForm()
    if form.validate_on_submit():
        new_application = Application(
            name=form.name.data, email=form.email.data, selected=form.radio.data)
        db.session.add(new_application)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('apply.htm', form=form)


@app.route('/admin')
@login_required
def admin_dashboard():
    if current_user.email1 == 'admin@studentigf.net':
        applications = Application.query.all()
        return render_template('admin.htm', applications=applications)
    return abort(403)


@app.route('/delete_application/<id>')
def delete_application(id):
    if current_user.email1 == 'admin@studentigf.net':
        application = Application.query.filter_by(id=id).first()
        db.session.delete(application)
        db.session.commit()
        return redirect(url_for('admin_dashboard'))
    return abort(403)

@app.route('/sigfz')
def sigfz():
    return render_template('sigfz.html')

if __name__ == '__main__':
    app.run(debug=True)
