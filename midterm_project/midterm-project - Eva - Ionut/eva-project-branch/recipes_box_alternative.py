import random


class RecipesBox(object):

    def __init__(self):
        self.recipes_box = {}

    def __getitem__(self, index):
        return self.recipes_box[index]

    def __delitem__(self, index):
        del self.recipes_box[index]

    def __setitem__(self, index, recipe):
        self.recipes_box[index] = recipe

    def __len__(self):
        return len(self.recipes_box)

    def insert(self, index, recipe):
        self.recipes_box.insert(index, recipe)

    def __iter__(self):
        return iter(self.recipes_box)

    def __str__(self):
        return f'Recipes Box: {list(self.recipes_box.keys())}'

    def add_recipe(self, recipe):
        self.recipes_box[recipe.name] = recipe.ingredients
        return f'Recipe {recipe.name} has been added to the Recipe Box'

    def delete_recipe(self, recipe):
        del self.recipes_box[recipe.name]
        return f'Recipe {recipe.name} has been removed from the Recipe Box'

    def pick_recipe(self, recipe = None):
        if not recipe:
            choices = list(self.recipes_box.keys())
            recipe_choice = random.choice(choices)
            return f'Here is a random recipe {recipe_choice} and the needed ingredients {self.recipes_box[recipe_choice]}'
        else:
            return f'Here is your recipe {recipe.name} and the needed ingredients {recipe.ingredients}'