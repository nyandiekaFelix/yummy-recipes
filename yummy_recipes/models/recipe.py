''' Models for Recipe Category and individual category '''

class RecipeCategory(object):
    ''' Recipe Category Model '''
    def __init__(self, category_name):
        self.category_name = category_name
        
    def __repr__(self):
        return '<%(category_name)s obj>' % dict(category_name=self.category_name)

class Recipe(object):
    ''' Recipe Model '''
    def __init__(self, category_name, recipe_name, ingredients, 
                 instructions):
        self.category_name = category_name
        self.recipe_name = recipe_name
        self.ingredients = ingredients
        self.instructions = instructions
        
    def __repr__(self):
        return '<%(recipe_name)s obj>' % dict(recipe_name=self.recipe_name)
        
