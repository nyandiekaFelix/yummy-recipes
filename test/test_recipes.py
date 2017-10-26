import unittest

from yummy_recipes import APP
from yummy_recipes.models.user import User
from yummy_recipes.models.recipe import RecipeCategory, Recipe

class TestRecipe(unittest.TestCase):
    ''' Test recipe categories and individual recipes '''
    def setUp(self):
         APP.WTF_CSRF_ENABLED = False
         self.user = User("name@domain.com", "Very_1secret")

    def test_recipe_category_creation(self):
        ''' should create category '''
        sample_category = RecipeCategory('Breakfast')
        self.user.categories[sample_category] = sample_category
        self.assertEqual(1, len(self.user.categories))

    def test_recipe_category_delete(self):
        ''' should delete recipe category '''
        new_category = RecipeCategory('Lunch')
        self.user.categories[new_category] = new_category
        self.assertEqual(1, len(self.user.categories))

        del self.user.categories[new_category]
        self.assertEqual(0, len(self.user.categories))
    
    def test_recipe_creation(self):
        ''' Should create recipe '''
        new_category = RecipeCategory('Supper')
        self.user.categories[new_category] = new_category

        recipe_name = 'cookie-stuff'
        ingredients = ['one', 'two', 'three', 'lastone']
        instructions = ['do this', 'do that', 'ha! go hungry loser']
        new_recipe = Recipe(recipe_name, ingredients, 
                            instructions)

        self.user.categories[new_category].recipes[new_recipe] = new_recipe
        
        self.assertEqual(1, len(self.user.categories[new_category].recipes))
        