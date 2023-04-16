from Tool import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name1 = db.Column(db.String(64))
    name2 = db.Column(db.String(64))
    name3 = db.Column(db.String(64))
    name4 = db.Column(db.String(64))

    school1 = db.Column(db.String(64))
    school2 = db.Column(db.String(64))
    school3 = db.Column(db.String(64))
    school4 = db.Column(db.String(64))

    email1 = db.Column(db.String(64))
    emailb = db.Column(db.String(64))

    phone1 = db.Column(db.Integer)
    phoneb = db.Column(db.Integer)
    am_name = db.Column(db.String(64))
    am_email = db.Column(db.String(64))
    am_phone = db.Column(db.Integer)

    password_hash = db.Column(db.String(128))

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __init__(self, password, name1, name2, name3, name4, school1, am_email, am_name, am_phone, school2, school3, school4, email1, emailb, phone1, phoneb):
        self.password_hash = generate_password_hash(password)
        self.name1 = name1
        self.name2 = name2
        self.name3 = name3
        self.name4 = name4
        self.school1 = school1
        self.school2 = school2
        self.school3 = school3
        self.school4 = school4
        self.email1 = email1
        self.emailb = emailb
        self.am_name = am_name
        self.am_email = am_email
        self.am_phone = am_phone
        self.phone1 = phone1
        self.phoneb = phoneb


class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    selected = db.Column(db.String(32))

    def __init__(self, name, email, selected):
        self.name = name
        self.email = email
        self.selected = selected

class SIGFChallengeSub(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    writeup = db.Column(db.String(150))
    school = db.Column(db.String)
    email = db.Column(db.String)
    age = db.Column(db.Integer)
    city = db.Column(db.String)
