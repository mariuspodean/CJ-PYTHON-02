import random
from collections.abc import MutableSequence, Mapping, MutableMapping
import copy

class PrettyPrinter:
    def __str__(self):
        name = self.name()
        dictionary = self.ingredients_dict()
        star_line = '*' * (len(name)+4) + '\n'
        string = star_line + '  '+ name + '\n'
        string += star_line + '\n'     
        for index, (keys, values) in enumerate(dictionary.items(), 1):
            string += f'  {index}. {keys}: {values} \n'
        string += '\n'
        string += star_line
        return (string)


class Recipe(PrettyPrinter, Mapping):
    
    def __init__(self, recipe_name, dictionary_of_ingredients):
        self._recipe_name = recipe_name
        self._dictionary_of_ingredients = dictionary_of_ingredients
        
    def __getitem__(self, ingredient):
        return self._dictionary_of_ingredients[ingredient]
       
    def __iter__(self):
        return iter(self._dictionary_of_ingredients)       
        
    def __len__(self):
        return len(self._dictionary_of_ingredients)
       
    def name(self):
        return copy.deepcopy(self._recipe_name)
    
    def ingredients_dict (self):
        return copy.deepcopy(self._dictionary_of_ingredients)
    
    def __str__(self):
        return super().__str__()
                    
class RecipesBox (MutableSequence):
   
    def __init__ (self, recipes_list):
        self.recipes_list = recipes_list
    
    def __iter__(self):
        return iter(self.recipes_list)
    
    def insert (self, index, recipe):
        return self.recipes_list(index, recipe)
    
    def __getitem__(self, index):
        return self.recipes_list[index]
    
    def __setitem__(self, index, value):
        self.recipes_list[index]=value
    
    def __delitem__(self, index):
        del self.recipes_list[index]
        
    def __len__(self):
        return len(recipes_list)
    
    def pick (self, recipe_to_extract=None):
        if recipe_to_extract:
            for recipe in self.recipes_list:
                if recipe.recipe_name == recipe_to_extract:
                    return recipe
        else:
            return random.choice(self.recipes_list)
    
    def add (self, recipe_to_add):
        self.recipes_list.append(recipe_to_add)
    
    def delete (self, recipe_to_delete):
        for recipe in self.recipes_list:
            if recipe.name() == recipe_to_delete:
                self.recipes_list.remove(recipe)
                break
    def __str__(self):
        names_list = []
        for recipe in self.recipes_list:
            names_list.append(recipe._recipe_name)
        return f'Lista de retete este {names_list}'
        

class Fridge(PrettyPrinter, MutableMapping):
    
    def __init__(self, fridge_name, dictionary_of_products):
        self.fridge_name = fridge_name
        self.dictionary_of_products = dictionary_of_products
        
    def __getitem__(self, product):
        return self.dictionary_of_products[product]
        
    def __setitem__(self, product, quantity):
        self.dictionary_of_products[product] = quantity
    
    def __iter__(self):
        return iter(self.dictionary_of_products)
    
    def __delitem__(self, product):
        del self.dictionary_of_products[product]
        
    def __len__(self):
        return len(self.dictionary_of_products)
        
    def add (self, product_name, product_quantity):
        previous_quantity=0
        if product_name in self.dictionary_of_products:
            previous_quantity = self.dictionary_of_products[product_name]
        self.dictionary_of_products[product_name] = previous_quantity + product_quantity
               
    def extract (self, product_name, product_quantity):
        if product_name in self.dictionary_of_products:
            if self.dictionary_of_products[product_name]>product_quantity:
                self.dictionary_of_products[product_name]-=product_quantity
            elif self.dictionary_of_products[product_name]<product_quantity:
                print (f'The quantity of {product_name} in the fridge is insufficient')
            else:
                del self.dictionary_of_products[product_name]
                print (f'Product {product_name} removed from the fridge')
        else:
            print ("Ingredient not in fridge")
                    
    def check_recipe (self, recipe):
        recipe_ingredients = set(recipe.dictionary_of_ingredients.keys())
        fridge_ingredients = set(dictionary_of_products.keys())
        available_ingredients = list(recipe_ingredients & fridge_ingredients)
        ingredients_to_be_bought = list(recipe_ingredients.difference(fridge_ingredients))
        print (f'Ingredients to be bought are {ingredients_to_be_bought} and available ingredients are {available_ingredients}')
        return (ingredients_to_be_bought, available_ingredients)
    
    def name (self):
        return self.fridge_name
    
    def ingredients_dict (self):
        return self.dictionary_of_products
    
    def __str__(self):
        return super().__str__()       

def check_the_fridge (fridge, recipes_box):
    recipes_from_the_fridge = []
    for recipe in recipes_box:
        recipe_ingredients = set(recipe.ingredients_dict().keys())
        fridge_ingredients = set(fridge.ingredients_dict().keys())
        common_ingredients = list(recipe_ingredients & fridge_ingredients)
        if len(common_ingredients) >= len(recipe_ingredients)/2:
            recipes_from_the_fridge.append(recipe.name())
    if not recipes_from_the_fridge:
        print (f'You don\'t have enough ingredients in the {fridge} for any of the recipes in your {recipes_box}')
    return recipes_from_the_fridge

shopping_list_archive=[]

def pretty_print_recipe(function):
    
    def inner_function(*args):
        shopping_dict = function(*args)
        if shopping_dict:
            string_to_print = r'''
                     ,---.           ,---.
                    / /"`.\.--"""--./,'"\ \
                    \ \    _       _    / /
                     `./  / __   __ \  \,'
                      /    /_O)_(_O\    \
                      |  .-'  ___  `-.  |
                   .--|       \_/       |--.
                 ,'    \   \   |   /   /    `.
                /       `.  `--^--'  ,'       \
             .-"""""-.    `--.___.--'     .-"""""-.
.-----------/         \------------------/         \------------.
| .---------\         /----------------- \         /----------. |
| |          `-`--`--'                    `--'--'-'           | |
| |                                                           | |
| |                       Shopping list                       | |
| |                                                           | |
'''
            for index, (keys, values) in enumerate(shopping_dict.items(), 1):
                current_line = f'| |{index}. {keys}: {values}'
                space_count = 62 - len (current_line)
                string_to_print += current_line + ' '*space_count + '| |\n'
            string_to_print += r'''| |___________________________________________________________| |
|_______________________________________________________________|
                   )__________|__|__________(
                  |            ||            |
                  |____________||____________|
                    ),-----.(      ),-----.(
                  ,'   ==.   \    /  .==    `.
                 /            )  (            \
                 `==========='    `===========' '''
            print (string_to_print)
        else:
            print ("The shopping list is empty")
                    
    return inner_function

def archive_shopping_list(function):
    
    def inner_function (*args):
        shopping_list_archive.append(function(*args))
        print ('List was archived')
        return function(*args)
    return inner_function


@pretty_print_recipe
@archive_shopping_list
def prepare_shopping_list(fridge, recipe):
    shopping_list = {}
    for ingredient, quantity in recipe.ingredients_dict().items():
        if ingredient in fridge.ingredients_dict():
            if fridge.ingredients_dict()[ingredient]<quantity:
                shopping_list[ingredient]=quantity-fridge.ingredients_dict()[ingredient]
        else:
            shopping_list[ingredient]=quantity
    return shopping_list


            
    




