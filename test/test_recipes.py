import unittest
from yummy_recipes.models.recipe import RecipeCategory, Recipe, CATEGORIES

class TestRecipe(unittest.TestCase):
    ''' Test recipe categories and individual recipes '''
    
    def test_recipe_category_creation(self):
        ''' should create category '''
        sample_category = RecipeCategory('Breakfast')
        CATEGORIES.append(sample_category)
        self.assertEqual(1, len(CATEGORIES))

    def test_recipe_category_delete(self):
        ''' should delete recipe category '''
        new_category = RecipeCategory('Lunch')
        CATEGORIES.append(new_category)
        self.assertEqual(2, len(CATEGORIES))

        CATEGORIES.remove(new_category)
        self.assertEqual(1, len(CATEGORIES))
    
    def test_recipe_creation(self):
        ''' Should create recipe '''
        new_category = RecipeCategory('Supper')
        CATEGORIES.append(new_category)

        recipe_name = 'cookie-stuff'
        description = 'Some short description'
        ingredients = ['one', 'two', 'three', 'lastone']
        instructions = ['do this', 'do that', 'ha! go hungry loser']
        new_recipe = Recipe(recipe_name, description, ingredients, 
                            instructions)

        CATEGORIES[1].recipes.append(new_recipe)
        print(CATEGORIES)
        self.assertEqual(1, len(CATEGORIES[1].recipes))
        