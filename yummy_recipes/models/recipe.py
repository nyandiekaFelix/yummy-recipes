from uuid import uuid4

''' Models for Recipe Category and individual category '''

class RecipeCategory(object):
    ''' Recipe Category Model '''
    def __init__(self, category_name):
        self.category_id = str(uuid4())
        self.category_name = category_name
        self.recipes = {}
        
    def __repr__(self):
        return '<%(category_name)s obj>' % dict(category_name=self.category_name)

class Recipe(object):
    ''' Individual Recipe Model '''
    def __init__(self, recipe_name, ingredients, 
                 instructions):
        self.recipe_id = str(uuid4())
        self.recipe_name = recipe_name
        self.ingredients = ingredients
        self.instructions = instructions
        
    def __repr__(self):
        return '<%(recipe_name)s obj>' % dict(recipe_name=self.recipe_name)
        
