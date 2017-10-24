from flask import session, render_template, redirect, request, url_for, flash

from yummy_recipes import APP
from yummy_recipes.forms import Login, Signup, RecipeForm, Category
from yummy_recipes.models.user import User, USERS
from yummy_recipes.models.recipe import RecipeCategory, Recipe

@APP.route('/')
@APP.route('/home')
def home():
    ''' Base route '''
    return render_template('home.html')

@APP.errorhandler(404)
def page_not_found(e):
    ''' 404 error handler '''
    return render_template('404.html')

@APP.route('/signup', methods=['POST', 'GET'])
def signup():
    ''' Create New user '''
    is_auth = False
    form = Signup()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        
        if email in USERS:
            flash("An account with that email already exists.")
        else:
            is_auth = True

            user = User(email, password)
            session['logged_in'] = True
            session['user'] = user.email
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
        
        if email in USERS and USERS[email].password == password:
                is_auth = True
                session['user'] = email
                session["logged_in"] = True
                return redirect(url_for('categories'))
        else:
            flash('Wrong Email or Password!')
    
    return render_template("login.html", form=form, is_auth=is_auth)

@APP.route('/logout')
def logout():
    ''' Log Out User '''
    session['logged_in'] = False
    return redirect(url_for('home'))
    
@APP.route('/categories', methods=['POST', 'GET'])
def categories():
    ''' Recipe Categories  '''
    categ_form = Category()
    

    if session.get('logged_in') is True:

        is_auth = True
        creator = session.get('user')
        user_categs = USERS[creator].categories

        if categ_form.validate_on_submit():
            category_name = categ_form.category_name.data

            if category_name in USERS[creator].categories:
                flash('That category already exists')            
            else:
                new_category = RecipeCategory(category_name)
                user_categs[new_category] = new_category
                
            return redirect(url_for('categories'))

    else:
        return redirect(url_for('categories'))     
    
    return render_template('recipes.html', is_auth=is_auth, categ_form=categ_form, 
                            categs=user_categs)

@APP.route('/recipes', methods=['POST', 'GET'])
def recipes():
    ''' Individual recipes '''
    form = RecipeForm()

    if session.get('logged_in') is True:
        is_auth = True
        creator = session.get('user')
        user_recs = USERS[creator].recipes

        if form.validate_on_submit():
            category_name = form.category_name.data
            recipe_name = form.recipe_name.data
            ingredients = form.ingredients.data
            instructions = form.instructions.data

            if recipe_name in user_recs:
                flash('A recipe with that name already exists')
            else:    
                new_recipe = Recipe(category_name, recipe_name, ingredients, instructions)
                user_recs[new_recipe] = new_recipe

                return redirect(url_for('recipes'))
    else:
        return redirect(url_for('recipes'))

    return render_template('recipes_detail.html', is_auth=is_auth, form=form, recs=user_recs)

