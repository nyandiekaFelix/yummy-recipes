import random

CATEGORIES = {}

class RecipeCategory(object):
    ''' Recipe Category Model '''
    def __init__(self, category_name, created_by=None):
        self.category_id = random.randint(1, 1000)
        self.category_name = category_name
        self.recipes = []
        self.created_by = created_by

class Recipe(object):
    ''' Recipe Model '''
    def __init__(self, recipe_name, description, ingredients, 
                instructions, created_by=None):
        self.recipe_id = random.randint(1, 1000)
        self.recipe_name = recipe_name
        self.description = description
        self.ingredients = ingredients
        self.instructions = instructions
        self.created_by = created_by

        
