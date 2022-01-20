from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, SubmitField, BooleanField,
    IntegerField
)
from wtforms.fields.choices import SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp


class RegistrationForm(FlaskForm):
    username = StringField(
        'Username', validators=[DataRequired(), Length(min=3, max=15)]
    )
    email = StringField(
        'Email', validators=[DataRequired(), Email()]
    )
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(min=5, max=20),
            Regexp('^(?=(.*[A-Z]){1,})(?=(.*[0-9]){1,}).{5,}$',
            message='Please include one at least one uppercase letter and one number'),
    ])
    password_check = PasswordField(
        'Confirm Password', validators=[DataRequired(), EqualTo('password')]
    )
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    username = StringField(
        'Username', validators=[DataRequired(), Length(min=3, max=15)]
    )
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(min=5, max=20)]
    )
    remember = BooleanField('Keep me signed up')
    submit = SubmitField('Log Me In')


class AddStock(FlaskForm):
    name = StringField(
        'Name', validators=[DataRequired(), Length(min=5, max=30)]
    )
    age = IntegerField(
        'Age', validators=[DataRequired()]
    )
    distillery = StringField('Distillery', validators=[DataRequired()])
    region = SelectField('Region', choices=(
        ('Campbeltown', 'Campbeltown'),
        ('Highland', 'Highland'),
        ('Islay','Islay'),
        ('Lowland', 'Lowland'),
        ('Speyside', 'Speyside')  
    ))
    notes = StringField('Additional Notes')
    image = StringField('Image Link')
    share = BooleanField()
    submit = SubmitField('Add to shelf')