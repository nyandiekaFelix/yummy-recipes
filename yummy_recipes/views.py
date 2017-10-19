from flask import session, render_template, redirect, request, url_for, flash

from yummy_recipes import APP
from yummy_recipes.forms import Login, Signup
from yummy_recipes.models.user import User, USERS
from yummy_recipes.models.recipe import RecipeCategory, Recipe, CATEGORIES  

@APP.route('/')
@APP.route('/home')
def home():
    return render_template('home.html')

@APP.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@APP.route('/signup', methods=['POST', 'GET'])
def signup():
    ''' Create New user '''
    form = Signup()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        first_name = form.first_name.data
        second_name = form.second_name.data
        password = form.password.data

        for user in USERS:
            if user.email == email:
                flash("An account with that email already exists.")
            else:
                user = User(email, first_name, second_name, password)
                return redirect(url_for('home'))
    
    return render_template("signup.html", form=form)

@APP.route('/login', methods=['POST', 'GET'])
def login():
    ''' Log In User '''

    form = Login()
    if request.method == 'POST':
        email = form.email.data
        password = form.password.data
        return redirect(url_for('home'))
        for user in USERS:
            if user.email == email:
                if user.password == password:
                    session["logged_in"] = True
                    session["email"] = user.email
                    return redirect(url_for('home'))
                else:
                    flash('Wrong password!')
            else:
                flash('User not found!')

    return render_template("login.html", form=form)

@APP.route('/myrecipes')
def my_recipes():
    return render_template('recipes.html')

@APP.route('/mycategories')
def my_categories():
    return render_template('recipe_category.html')