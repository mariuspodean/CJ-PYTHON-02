
class Recipe:
    def __init__(self, name, ingredients): 
        self. name = name
        self.ingredients = ingredients
    def __getitem__ (self, key):
        return self.ingredients[key]
    def __iter__(self):
        return iter(self.ingredients)
    def __len__ (self):
        return len (self.ingredients)


class PrettyPrinter:
    def pretty_printer(recipe):
        print("*" * 30)
        print(recipe.name)
        print("*" * 30)
        for index, (ingredient, quantity) in enumerate (recipe.ingredients.items(), start = 1):
            print(f'{index}{"."} {ingredient}{":"}{quantity}')
        print("*" * 30)

class PrintRecipe (Recipe, PrettyPrinter):
    pass


class RecipesBox:
    def __init__(self, iterable):
        self.recipes = list(iterable)
    def __getitem__ (self, index):
        return self.recipes[index]
    def __setitem__(self, index, recipe):
        self.recipes[index] = recipe
    def __delitem__(self, index):
        return self.recipes.pop(index)
    def __len__ (self):
        return len (self.recipes)
    def pick(self, name=None):
        for recipe in self.recipes:
            if recipe.name == name:
                return recipe
        return self.recipes[0]



class Fridge(object):
    def __init__(self):
        self.ingredients = {}
    def __iter__(self):
        return iter(self.ingredients)
    def __len__ (self):
        return len (self.ingredients)
    def __getitem__ (self, ingredient):
        return self.ingredients[ingredient]
    def __delitem__(self, ingredient):
        return self.ingredients[ingredient]
    def __setitem__(self, ingredient, volume):
        self.ingredients[ingredient] = volume
        return f'The amount of {ingredient} available is {volume}'
    def __str__(self):
        frame = '*' * 25
        print ('\n', frame, '\n Ingredients in fridge:')
        print (self.ingredients)
        return frame
       
    def add_ingredient (self, ingredient, volume):
        self.ingredients[ingredient] = volume
        print (f' Ingredient {ingredient} has been added in the fridge')
    def update_volume (self, ingredient, volume):
        if volume > 0:
            self.ingredients[ingredient] = volume
            print (f'The volume of {ingredient} has changed to {volume}')
        else:
            print ('The ingredient is no longer available in the fridge')
    def delete_ingredient (self, ingredient, volume):
        del self.ingredients[ingredient]
        print (f'Ingredient {ingredient} is no longer in the fridge')


    def check_recipe (self, recipe):
        ingredients_to_purchase = []
        ingredients_available = []
        for ingredient in recipe.ingredients.keys():
            ingredients_available.append(ingredient)
        else:
            ingredients_to_purchase.append(ingredient)
        return ingredients_available, ingredients_to_purchase


def check_the_fridge(fridge, recipes_box):
    list_recipes = []
    for recipe in recipes_box.recipes:
        ingredients_count = 0
        for ingredient in recipe.ingredients.keys():
            if ingredient in fridge.ingredients:
                ingredients_count = ingredients_count + 1
        if len (recipe.ingredients.keys() )/2 <= ingredients_count:
            list_recipes.append(recipe.name) 
    return list_recipes

def pretty_print_recipe(func):
    def wrapper(fridge, recipe):
        func(fridge,recipe)
        print("    /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\ ",
      '\n   //\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\ ',
      '\n  //\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\/\ ',
      '\n //\\ \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \ ')
        print('            Shopping list:')
        for elem in shopping_list_archive:
            for index, (ingredient, volume) in enumerate (elem.items(), start = 1):
                print(f'{index}{". "}{ingredient}{": "}{volume}')
        print("    /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\ ",
      '\n   //\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\ ',
      '\n  //\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\/\ ',
      '\n //\\ \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \ ')

    return wrapper

shopping_list_archive = []
def archive_shopping_list (func):
    def wraper(fridge, recipe):
        to_buy_list =  func(fridge,recipe)
        shopping_list_archive.append (to_buy_list)
    return wraper
    

@pretty_print_recipe
@archive_shopping_list
def prepare_shopping_list(fridge, recipe):
    to_buy_list = {}
    for ingredient, volume in recipe.ingredients.items():
        if ingredient not in fridge.ingredients:
            to_buy_list[ingredient] = volume
        else:
            if volume > fridge.ingredients[ingredient]:
                to_buy_list[ingredient] = volume - fridge.ingredients[ingredient]
    return to_buy_list
