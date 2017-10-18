from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, IntegerField
from wtforms.validators import Length, Email, InputRequired, DataRequired, Regexp, EqualTo, Optional

class Signup(Form):
    ''' User registration form '''
    email = StringField('Email:', validators=[Email(), InputRequired()])

    first_name = StringField('First Name:', 
                                validators=[InputRequired(),
                                DataRequired(),
                                Regexp("^[A-Za-z_-]*$", 0, 
                                'Use letters only and no spaces')])

    second_name = StringField('Second Name:', validators=[InputRequired(),
                                DataRequired(),
                                Regexp("^[A-Za-z_-]*$", 0,
                                        'Use letters only and no spaces')])

    password = PasswordField('Password:', validators=[Length(6, 25), InputRequired(), 
                EqualTo('password_confirm', 
                message=(u'Passwords Do Not Match')),
                Regexp("^(?=.*?[A-Z]).*[0-9]",  0,
                        'Should contain atleast one digit and one uppercase letter')])

    password_confirm = PasswordField('Confirm password')
    submit = SubmitField('Sign Up')

class Login(Form):
    ''' User log in form '''
    email = StringField('Email:', validators=[Email(), InputRequired()])
    password = PasswordField('Password:', validators=[InputRequired()])
    submit = SubmitField('Log In')