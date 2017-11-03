from flask_wtf import Form
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import Email, InputRequired, DataRequired, Regexp, EqualTo, Length

class Signup(Form):
    ''' User registration form '''
    email = StringField('Email:', validators=[Email(), InputRequired()])
    password = PasswordField('Password:', validators=[InputRequired(), Length(min=4, max=25),
                EqualTo('password_confirm', 
                message=(u'Passwords Do Not Match')),
                Regexp("^(?=.*?[A-Z]).*[0-9]",  0,
                        'Should contain letters and at least one digit and one uppercase letter')])

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
                                        Regexp("^[A-Za-z]+( +[A-Za-z]+)*$",
                                                0,
                                                'Use only letters and spaces')])

class RecipeForm(Form):
    ''' individual recipes form '''
    recipe_name = StringField(
        'Recipe Name: ', validators=[InputRequired(),
                                        DataRequired(),
                                        Regexp("^[A-Za-z]+( +[A-Za-z]+)*$",
                                                0,
                                                'Use only letters and spaces')])
    ingredients = StringField(
        'Ingredients: ', validators=[InputRequired(), Length(min=5, max=200),
                                        DataRequired()])
    
    instructions = StringField(
        'Instructions: ', validators=[InputRequired(), Length(min=5, max=200),
                                        DataRequired()])
    
