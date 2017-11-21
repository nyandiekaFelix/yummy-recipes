from flask import session, render_template, redirect, request, url_for, flash

from yummy_recipes import APP
from yummy_recipes.forms import LoginForm, SignupForm, RecipeForm, CategoryForm
from yummy_recipes.models.user import User, USERS
from yummy_recipes.models.recipe import RecipeCategory, Recipe
from yummy_recipes.helpers import lower_email, check_for_duplicate


@APP.route('/')
@APP.route('/home')
def home():
    ''' The base route. It directs the user to a home page
    with a welcome message '''

    if (session.get('logged_in') and
            session.get('user') in USERS):

        is_auth = True
    else:
        is_auth = False

    return render_template('home.html', is_auth=is_auth)


@APP.errorhandler(404)
def page_not_found(err):
    ''' 404 error handler '''
    if (session.get('logged_in') and
            session.get('user') in USERS):

        is_auth = True
    else:
        is_auth = False

    return render_template('404.html', is_auth=is_auth)


@APP.route('/signup', methods=['POST', 'GET'])
def signup():
    ''' This route handles creation of a new user '''
    is_auth = False
    if (session.get('logged_in') and
            session.get('user') in USERS):

        is_auth = True
        return redirect(url_for('categories'))
    form = SignupForm()
    if form.validate_on_submit():
        email = lower_email(form.email.data)
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
    ''' This route handles logging in of users '''
    is_auth = False
    if (session.get('logged_in') and
            session.get('user') in USERS):

        is_auth = True
        return redirect(url_for('categories'))
    form = LoginForm()
    if form.validate_on_submit():
        email = lower_email(form.email.data)
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
    ''' This route handles creation and viewing of recipe Categories '''
    categ_form = CategoryForm()
    if (session.get('logged_in') and
            session.get('user') in USERS):

        is_auth = True
        creator = session.get('user')
        user_categs = USERS[creator].categories

        if categ_form.validate_on_submit():
            category_name = categ_form.category_name.data.lower()
            category_exists = check_for_duplicate(user_categs, category_name)

            if category_exists:
                flash('That category already exists')
            else:
                new_category = RecipeCategory(category_name)
                user_categs[new_category.category_id] = new_category
                flash('Category created')
            return redirect(url_for('categories'))

    else:
        is_auth = False
        return redirect(url_for('login'))
    return render_template('recipes.html', is_auth=is_auth,
                           categ_form=categ_form, categs=user_categs)


@APP.route('/recipes', methods=['POST', 'GET'])
def recipes():
    ''' This route handles creation and viewing of recipes '''
    rec_form = RecipeForm()
    if (session.get('logged_in') and
            session.get('user') in USERS):

        is_auth = True
        creator = session.get('user')
        categs = USERS[creator].categories
        if rec_form.validate_on_submit():
            category_id = request.form.get('categ_id')
            recipe_name = rec_form.recipe_name.data.lower()
            ingredients = rec_form.ingredients.data
            instructions = rec_form.instructions.data

            if not category_id:
                flash('Category field is required')
            else:
                category_recipes = categs[category_id].recipes

                recipe_exist = check_for_duplicate(category_recipes,
                                                   recipe_name)

                if recipe_exist:
                    flash('A recipe with that name exists')
                else:
                    # instanciate a new recipe
                    new_recipe = Recipe(recipe_name, ingredients, instructions)
                    parent_category = categs[category_id]
                    parent_category.recipes[new_recipe.recipe_id] = new_recipe
                    flash('recipe created')
            return redirect(url_for('recipes'))

    else:
        is_auth = False
        return redirect(url_for('login'))
    return render_template('recipes_detail.html', is_auth=is_auth,
                           form=rec_form, categs=categs)


@APP.route('/edit_recipe', methods=['POST'])
def edit_recipe():
    ''' This route handles the editing of recipes ased on the user's input '''
    rec_form = CategoryForm()

    if (session.get('logged_in') and
            session.get('user') in USERS):

        is_auth = True
        creator = session.get('user')
        categs = USERS[creator].categories

        recipe_id = request.form.get('recipe_id')
        category_id = request.form.get('categ_id')
        new_title = request.form.get('new_title').lower()
        new_ingredients = request.form.get('new_ingredients')
        new_instructions = request.form.get('new_instructions')

        category_recipes = categs[category_id].recipes

        # check if the recipe name is a duplicate
        recipe_exists = check_for_duplicate(category_recipes, new_title)

        if recipe_exists is True:
            flash('A recipe with that name exists')
        else:
            recipe_to_edit = categs[category_id].recipes[recipe_id]

            recipe_to_edit.recipe_name = (new_title if new_title
                                          else recipe_to_edit.recipe_name)
            recipe_to_edit.ingredients = (new_ingredients if new_ingredients
                                          else recipe_to_edit.ingredients)
            recipe_to_edit.instructions = (new_instructions if new_instructions
                                           else recipe_to_edit.instructions)
            flash('recipe updated')

        return redirect(url_for('recipes'))
    else:
        is_auth = False
    return render_template('recipes.html', is_auth=is_auth, form=rec_form,
                           categs=categs)


@APP.route('/delete_recipe', methods=['POST'])
def delete_recipe():
    ''' This route handles deleting of recipes  '''
    rec_form = CategoryForm()

    if (session.get('logged_in') and
            session.get('user') in USERS):

        is_auth = True
        creator = session.get('user')
        categs = USERS[creator].categories

        recipe_id = request.form.get('recipe_id')
        category_id = request.form.get('categ_id')

        if category_id in categs:
            del categs[category_id].recipes[recipe_id]
            flash('recipe deleted')
        else:
            flash('Recipe Not Found')
        return redirect(url_for('recipes'))

    else:
        is_auth = False
    return render_template('recipes.html', is_auth=is_auth, form=rec_form,
                           categs=categs)


@APP.route('/edit_category', methods=['POST', 'GET'])
def edit_category():
    ''' This route handles updating of recipe categories  '''
    categ_form = CategoryForm()

    if (session.get('logged_in') and
            session.get('user') in USERS):

        is_auth = True
        creator = session.get('user')
        user_categs = USERS[creator].categories

        category_id = request.form.get('categ_id')
        new_name = request.form.get('new_name').lower()

        category_exists = check_for_duplicate(user_categs, new_name)

        if category_exists is True:
            flash('That category already exists')
        else:
            user_categs[category_id].category_name = new_name
            flash('Category updated')

        return redirect(url_for('categories'))

    else:
        is_auth = False
    return render_template('recipes.html', is_auth=is_auth,
                           categ_form=categ_form, categs=user_categs)


@APP.route('/del_category', methods=['POST'])
def delete_category():
    ''' This route handles deleting of recipe categories  '''
    categ_form = CategoryForm()

    if (session.get('logged_in') and
            session.get('user') in USERS):

        is_auth = True
        creator = session.get('user')
        categs = USERS[creator].categories

        category_id = request.form.get('categ_id')
        if category_id in categs:
            del categs[category_id]
            flash('category deleted')
        else:
            flash('Category Not Found')

        return redirect(url_for('categories'))

    else:
        is_auth = False
    return render_template('recipes.html', is_auth=is_auth,
                           categ_form=categ_form, categs=categs)
