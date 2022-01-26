# Credit for using Flask wtforms to Corey Schafer - Python Flask Tutorial

from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, SubmitField, BooleanField,
    IntegerField
)
from wtforms.fields.choices import SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp


'''
Registration Form is stored as a class and each input validation requirement is
defined using the wtforms validators. Validators check the inputs once
form.validate_on_submit() is called. Errors raised based on these validators
can be picked up by the JQuery form validation plugin on client side.
'''


class RegistrationForm(FlaskForm):
    username = StringField(
        'Username - Only letters and numbers',
        validators=[
            DataRequired(), Length(min=3, max=15),
            # Use Regex to check that username does not contain special chars
            Regexp(
                '^(?=.*[a-z])\w{3,}$',
                message='No special characters allowed'
            ),
        ]
    )
    email = StringField(
        # Use Email validator to check the email format is valid
        'Email', validators=[DataRequired(), Email()]
    )
    password = PasswordField(
        'Password - Must include at least one uppercase letter and one number',
        validators=[
            DataRequired(), Length(min=5, max=20),
            # Use Regex to check that password includes 1 upper letter and 1 nr
            Regexp(
                '^(?=(.*[A-Z]){1,})(?=(.*[0-9]){1,}).{5,}$',
                message='Your password does not meet the requirements'
            ),
        ]
    )
    password_check = PasswordField(
        # Use EqualTo validator to match password inputs
        'Confirm Password', validators=[DataRequired(), EqualTo('password')]
    )
    submit = SubmitField('Submit')


'''
Registration Form is stored as a class and each input validation requirement is
defined using the wtforms validators. Validators check the inputs once
form.validate_on_submit() is called. Errors raised based on these validators
can be picked up by the JQuery form validation plugin on client side.
'''


class LoginForm(FlaskForm):
    username = StringField(
        'Username', validators=[DataRequired(), Length(min=3, max=15)]
    )
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(min=5, max=20)]
    )
    remember = BooleanField('Keep me signed up')
    submit = SubmitField('Log Me In')


'''
Registration Form is stored as a class and each input validation requirement is
defined using the wtforms validators. Validators check the inputs once
form .validate_on_submit() is called. Errors raised based on these validators
can be picked up by the JQuery form validation plugin on client side.
'''


class AddStock(FlaskForm):
    name = StringField(
        'Name', validators=[DataRequired(), Length(min=5, max=50)]
    )
    age = IntegerField(
        'Age', validators=[DataRequired()]
    )
    distillery = StringField('Distillery', validators=[DataRequired()])
    region = SelectField('Region', choices=(
        ('Campbeltown', 'Campbeltown'),
        ('Highland', 'Highland'),
        ('Islay', 'Islay'),
        ('Lowland', 'Lowland'),
        ('Speyside', 'Speyside')
    ))
    notes = StringField('Additional Notes')
    image = StringField('Image Link')
    share = BooleanField()
    submit = SubmitField('Add to shelf')
