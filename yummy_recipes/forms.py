from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, IntegerField
from wtforms.validators import Length, Email, InputRequired, DataRequired, Regexp, EqualTo, Optional

class Signup(Form):
    ''' User registration form '''
    email = StringField('Email:', validators=[Email(), InputRequired()])
    password = PasswordField('Password:', validators=[InputRequired(), 
                EqualTo('password_confirm', 
                message=(u'Passwords Do Not Match')),
                Regexp("^(?=.*?[A-Z]).*[0-9]",  0,
                        'Should contain atleast one digit and one uppercase letter')])

    password_confirm = PasswordField('Confirm password:')
    
class Login(Form):
    ''' User log in form '''
    email = StringField('Email:', validators=[Email(), InputRequired()])
    password = PasswordField('Password:', validators=[InputRequired()])
    
class Category(Form):
    ''' Recipe Category Form '''
    category_name = StringField(
        'New Category:', validators=[InputRequired(),
                                        DataRequired(),
                                        Regexp("^[A-Za-z0-9_-]+( +[A-Za-z0-9_-]+)*$",
                                                0,
                                                'Use only letters numbers and spaces')])

class Recipe(Form):
    recipe_name = StringField(
        'Recipe Name: ', validators=[InputRequired(),
                                        DataRequired(),
                                        Regexp("^[A-Za-z0-9_-]+( +[A-Za-z0-9_-]+)*$",
                                                0,
                                                'Use only letters numbers and spaces')])
    description = StringField(
        'Description: ', validators=[InputRequired(),
                                        DataRequired(),
                                        Regexp("^[A-Za-z0-9_-]+( +[A-Za-z0-9_-]+)*$",
                                                0,
                                                'Use only letters numbers and spaces')])
    
    Ingredients = StringField(
        'Ingredients: ', validators=[InputRequired(),
                                        DataRequired(),
                                        Regexp("^[A-Za-z0-9_-]+( +[A-Za-z0-9_-]+)*$",
                                                0,
                                                'Use only letters numbers and spaces')])
    
    Instructions = StringField(
        'Instructions: ', validators=[InputRequired(),
                                        DataRequired(),
                                        Regexp("^[A-Za-z0-9_-]+( +[A-Za-z0-9_-]+)*$",
                                                0,
                                                'Use only letters numbers and spaces')])
    