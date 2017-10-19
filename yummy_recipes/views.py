from flask import session, render_template, redirect, request, url_for, flash

from yummy_recipes import APP
from yummy_recipes.forms import Login, Signup, Recipe, Category
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
    is_auth = False
    form = Signup()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        first_name = form.first_name.data
        second_name = form.second_name.data
        password = form.password.data
        
        if email in USERS:
            flash("An account with that email already exists.")
        else:
            user = User(email, first_name, second_name, password)
            session['logged_in'] = True
            session['email'] = user.email
            session['password'] = password
            USERS[email] = user

            return redirect(url_for('categories'))
       
    return render_template("signup.html", form=form, is_auth=is_auth)

@APP.route('/login', methods=['POST', 'GET'])
def login():
    ''' Log In User '''
    is_auth = False

    form = Login()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        
        if session.get('email') == email and\
            session.get('password') == password:
                session['email'] = email
                session["logged_in"] = True
                return redirect(url_for('categories'))
        else:
            flash('Wrong Email or Password!')
    
    return render_template("login.html", form=form, is_auth=is_auth)

@APP.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(url_for('home'))
    
@APP.route('/categories', methods=['POST', 'GET'])
def categories():
    
    form = Category()

    if 'email' in session:
        is_auth = True

        if form.validate_on_submit():
            category_name = form.category_name.data
            created_by = session.get('email')
            recipe_category = RecipeCategory(category_name, created_by)
            
            if category_name in CATEGORIES:
                flash('That category already exists')            
            else:
                CATEGORIES[recipe_category] = recipe_category
                    
            return redirect(url_for('categories'))

    else:
        is_auth = False
        return redirect(url_for('login'))     
    
    return render_template('recipe_category.html', is_auth=is_auth, form=form, categs=CATEGORIES)

@APP.route('/recipes')
def recipes():

    if 'email' in session:
        is_auth = True
    else:
        is_auth = False  

    return render_template('recipes.html', is_auth=is_auth)

