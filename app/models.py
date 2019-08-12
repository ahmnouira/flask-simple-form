from app import db
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash


class Users(db.Document):
    first_name = db.StringField(max_length=64)
    last_name = db.StringField(max_length=64)
    email = db.StringField(max_length=64)
    password = db.StringField(max_length=64)
    password_hash = db.StringField(max_length=128, required=False)
    company = db.StringField(max_length=128, required=False)
    city = db.StringField(max_length=128, required=False)
    state = db.StringField(required=False)

    # get user full_name
    def full_name(self):
        return str(self.first_name + " " + self.last_name)

    # set_password
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # check_password
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # for User object representation
    def __repr__(self):
        return "< User : {} {}>".format(self.first_name, self.last_name)
