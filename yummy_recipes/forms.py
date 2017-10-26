from flask_wtf import Form
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import Email, InputRequired, DataRequired, Regexp, EqualTo

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

class RecipeForm(Form):
    ''' individual recipes form '''
    recipe_name = StringField(
        'Recipe Name: ', validators=[InputRequired(),
                                        DataRequired(),
                                        Regexp("^[A-Za-z0-9_-]+( +[A-Za-z0-9_-]+)*$",
                                                0,
                                                'Use only letters numbers and spaces')])
    ingredients = StringField(
        'Ingredients: ', validators=[InputRequired(),
                                        DataRequired()])
    
    instructions = StringField(
        'Instructions: ', validators=[InputRequired(),
                                        DataRequired()])
    