from flask import session, render_template, redirect, request, url_for, flash

from yummy_recipes import APP
from yummy_recipes.forms import Login, Signup
from yummy_recipes.models.user import User, USERS
from yummy_recipes.models.recipe import RecipeCategory, Recipe, CATEGORIES  

@APP.route('/')
def home():
    pass

@APP.route('/myrecipes')
def my_recipes():
    pass

@APP.route('/signup', methods=['POST', 'GET'])
def signup():
    ''' Create New user '''
    form = Signup()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        password = form.password.data
        if USERS:
            for user in USERS:
                if user.email == email:
                    flash("An account with that email already exists.")
                else:
                    user = User(email, first_name, last_name, password)
                    USERS.append(user)
                    return redirect(url_for('myrecipes'))
        else:
            user = User(email, first_name, last_name, password)
            USERS.append(user)
            return redirect(url_for('myrecipes'))
        
        return render_template("signin.html", form=form)

@APP.route('/login', methods=['POST', 'GET'])
def login():
    ''' Log In User '''

    form = Login()
    if request.method == 'POST':
        email = form.email.data
        password = form.password.data
        for user in USERS:
            if user.email == email:
                if user.password == password:
                    session["logged_in"] = True
                    session["email"] = user.email
                    return redirect(url_for('myrecipes'))
                else:
                    flash('Wrong password!')
            else:
                flash('User not found!')
    return render_template("login.html", form=form)
