from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField(
        'Username', validators=[DataRequired(), Length(min=3, max=15)]
    )
    email = StringField(
        'Email', validators=[DataRequired(), Email()]
    )
    password = PasswordField(
        'Passwprd', validators=[DataRequired(), Length(min=5, max=20),]
    )
    password_check = PasswordField(
        'Confirm Password', validators=[DataRequired, EqualTo('password')]
    )
    submit = SubmitField('Register')