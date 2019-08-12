from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import Users as User


class UserForm(FlaskForm):
    first_name = StringField('First name:', validators=[DataRequired()])
    last_name = StringField('Last:', validators=[DataRequired()])
    email = StringField('Email:', validators=[DataRequired(), Email()])
    password = PasswordField('Password:', validators=[DataRequired()])
    company = StringField('Company: ')
    city = StringField('City: ')
    state = StringField('State :')
    submit = SubmitField("submit")


    def validate_email(self, email):
        user = User.query.filter(User.email == email.data).first()
        if user is not None:
            print('This email is taken !!')
            raise ValidationError('This email is taken !!')
