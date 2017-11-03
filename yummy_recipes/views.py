from flask import session, render_template, redirect, request, url_for, flash

from yummy_recipes import APP
from yummy_recipes.forms import Login, Signup, RecipeForm, Category
from yummy_recipes.models.user import User, USERS
from yummy_recipes.models.recipe import RecipeCategory, Recipe


@APP.route('/')
@APP.route('/home')
def home():
    ''' Base route '''
    if session.get('logged_in') is True and\
            session.get('user') in USERS:

        is_auth = True
    else:
        is_auth = False

    return render_template('home.html', is_auth=is_auth)

@APP.errorhandler(404)
def page_not_found(err):
    ''' 404 error handler '''
    if session.get('logged_in') is True and\
            session.get('user') in USERS:

        is_auth = True
    else:
        is_auth = False

    return render_template('404.html', is_auth=is_auth)

@APP.route('/signup', methods=['POST', 'GET'])
def signup():
    ''' Create New user '''
    is_auth = False
    if session.get('logged_in') is True and\
            session.get('user') in USERS:

        is_auth = True
        return redirect(url_for('categories'))
   
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
    if session.get('logged_in') is True and\
            session.get('user') in USERS:

        is_auth = True
        return redirect(url_for('categories'))
    
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
    session.pop('user')
    return render_template('home.html', is_auth=False)
    
@APP.route('/categories', methods=['POST', 'GET'])
def categories():
    ''' Recipe Categories  '''
    categ_form = Category()
    

    if session.get('logged_in') is True and\
            session.get('user') in USERS:

        is_auth = True
        creator = session.get('user')
        user_categs = USERS[creator].categories

        if categ_form.validate_on_submit():
            category_name = categ_form.category_name.data
            
            if category_name in user_categs.values():
                flash('That category already exists')            
            else:
                new_category = RecipeCategory(category_name)
                user_categs[new_category.category_id] = new_category
                flash('Category created')
                
            return redirect(url_for('categories'))

    else:
        is_auth = False
        
    return render_template('recipes.html', is_auth=is_auth, 
                            categ_form=categ_form, categs=user_categs)

@APP.route('/recipes', methods=['POST', 'GET'])
def recipes():
    ''' Individual recipes '''
    rec_form = RecipeForm()
    
    if session.get('logged_in') is True and\
            session.get('user') in USERS:
        is_auth = True
        creator = session.get('user')
        categs = USERS[creator].categories

        if rec_form.validate_on_submit():
            category_id = request.form.get('categ_id')
            recipe_name = rec_form.recipe_name.data
            ingredients = rec_form.ingredients.data
            instructions = rec_form.instructions.data

            new_recipe = Recipe(recipe_name, ingredients, instructions)
            
            if category_id in categs:
                categs[category_id].recipes[new_recipe.recipe_id] = new_recipe
            else:
                flash('category does not exist')
            return redirect(url_for('recipes'))

    else:
        is_auth = False
     
    return render_template('recipes_detail.html', is_auth=is_auth, 
                            form=rec_form, categs=categs)

@APP.route('/edit_recipe', methods=['POST'])
def edit_recipe():
    rec_form = Category()

    if session.get('logged_in') is True and\
            session.get('user') in USERS:
        is_auth = True
        creator = session.get('user')
        categs = USERS[creator].categories

        recipe_id = request.form.get('recipe_id')
        category_id = request.form.get('categ_id')
        new_title = request.form.get('new_title')
        new_ingredients = request.form.get('new_ingredients')
        new_instructions = request.form.get('new_instructions')

        categs[category_id].recipes[recipe_id].recipe_name = new_title
        categs[category_id].recipes[recipe_id].ingredients = new_ingredients
        categs[category_id].recipes[recipe_id].instructions = new_instructions

        return redirect(url_for('recipes'))
    else:
        is_auth = False
   
    return render_template('recipes.html', is_auth=is_auth, form=rec_form, 
                            categs=categs)

    

@APP.route('/del_recipe', methods=['POST'])
def del_recipe():

    rec_form = Category()

    if session.get('logged_in') is True and\
            session.get('user') in USERS:
        is_auth = True
        creator = session.get('user')
        categs = USERS[creator].categories

        recipe_id = request.form.get('recipe_id')
        category_id = request.form.get('categ_id')

        if category_id in categs:
            del categs[category_id].recipes[recipe_id]
        else:
            flash('Recipe Not Found')
            
        return redirect(url_for('recipes'))

    else:
        is_auth = False
        
    return render_template('recipes.html', is_auth=is_auth, form=rec_form, 
                            categs=categs)

@APP.route('/edit_category', methods=['POST', 'GET'])
def edit_category():
    categ_form = Category()

    if session.get('logged_in') is True and\
            session.get('user') in USERS:
        is_auth = True
        creator = session.get('user')
        categs = USERS[creator].categories

        category_id = request.form.get('categ_id')
        new_name = request.form.get('new_name')

        categs[category_id].category_name = new_name
        
        return redirect(url_for('categories'))

    else:
        is_auth = False
        
    return render_template('recipes.html', is_auth=is_auth, 
                            categ_form=categ_form, categs=categs)


@APP.route('/del_category', methods=['POST'])
def del_category():
    categ_form = Category()

    if session.get('logged_in') is True and\
            session.get('user') in USERS:
        is_auth = True
        creator = session.get('user')
        categs = USERS[creator].categories

        category_id = request.form.get('categ_id')
        
        if category_id in categs:
            del categs[category_id]
        else:
            flash('Category Not Found')

        return redirect(url_for('categories'))

    else:
        is_auth = False
        
    return render_template('recipes.html', is_auth=is_auth, 
                            categ_form=categ_form, categs=categs)


