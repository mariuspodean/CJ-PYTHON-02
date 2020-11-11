import random
from collections.abc import MutableSequence, Mapping, MutableMapping

class PrettyPrinter:
    
    def __str__(self):
        name = self.name
        star_line = '*' * (len(name)+4) + '\n'
        string = star_line + '  '+ name + '\n'
        string += star_line + '\n'     
        for index, (keys, values) in enumerate(self.items(), 1):
            string += f'  {index}. {keys}: {values} \n'
        string += '\n'
        string += star_line
        return (string)

#taken from https://stackoverflow.com/questions/19022868/how-to-make-dictionary-read-only-in-python
class ReadOnlyDict(dict):
    
    def __readonly__(self, *args, **kwargs):
        raise RuntimeError("Cannot modify Recipe")
    
    __setitem__ = __readonly__
    __delitem__ = __readonly__
    pop = __readonly__
    popitem = __readonly__
    clear = __readonly__
    update = __readonly__
    setdefault = __readonly__
    del __readonly__
    
class Recipe(PrettyPrinter):
    
    def __init__(self, name, dictionary_of_ingredients):
        self._name = name
        self._dictionary_of_ingredients = ReadOnlyDict(dictionary_of_ingredients)
    
    @property
    def name(self):
        return self._name

    def __getitem__(self, ingredient):
        return self._dictionary_of_ingredients[ingredient]
    
    def __contains__(self, ingredient):
        if ingredient in self._dictionary_of_ingredients:
            return True
        else:
            return False
    def get(self, key):
        return self._dictionary_of_ingredients[key]
    
    def __eq__(self, other):
        if isinstance(other, Recipe):
            return self._dictionary_of_ingredients == other._dictionary_of_ingredients
        return False
    
    def __ne__(self, other):
        return not self.__eq__(other)
       
    def __iter__(self):
        return iter(self._dictionary_of_ingredients)       
        
    def __len__(self):
        return len(self._dictionary_of_ingredients)
    
    def items(self):
        return self._dictionary_of_ingredients.items()
    
    def keys(self):
        return self._dictionary_of_ingredients.keys()
    
    def values(self):
        return self._dictionary_of_ingredients.values()
       
    def __str__(self):
        return super().__str__()
                    
class RecipesBox():
   
    def __init__ (self, name, recipes_list):
        self.name=name
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
                if recipe.name == recipe_to_extract:
                    return recipe
        else:
            return random.choice(self.recipes_list)
    
    def add (self, recipe_to_add):
        self.recipes_list.append(recipe_to_add)
    
    def delete (self, recipe_to_delete):
        for recipe in self.recipes_list:
            if recipe.name == recipe_to_delete:
                self.recipes_list.remove(recipe)
                break
    def __str__(self):
        names_list = []
        for recipe in self.recipes_list:
            names_list.append(recipe._name)
        return f'Lista de retete este {names_list}'
        

class Fridge(PrettyPrinter):
    
    def __init__(self, name, dictionary_of_products):
        self.name = name
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
    
    def items(self):
        return self.dictionary_of_products.items()
    
    def keys(self):
        return self.dictionary_of_products.keys()
    
    def values(self):
        return self.dictionary_of_products.values()
        
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
        recipe_ingredients = set(recipe.keys())
        fridge_ingredients = set(self.dictionary_of_products.keys())
        available_ingredients = list(recipe_ingredients & fridge_ingredients)
        ingredients_to_be_bought = list(recipe_ingredients.difference(fridge_ingredients))
        print (f'For the {recipe.name}, ingredients to be bought are {ingredients_to_be_bought} and available ingredients are {available_ingredients}')
        return (ingredients_to_be_bought, available_ingredients)
    
    def __str__(self):
        return super().__str__()       

def check_the_fridge (fridge, recipes_box):
    recipes_from_the_fridge = []
    for recipe in recipes_box:
        recipe_ingredients = set(recipe.keys())
        fridge_ingredients = set(fridge.keys())
        common_ingredients = list(recipe_ingredients & fridge_ingredients)
        if len(common_ingredients) >= len(recipe_ingredients)/2:
            recipes_from_the_fridge.append(recipe.name())
    if not recipes_from_the_fridge:
        print (f'You don\'t have enough ingredients in the {fridge.name} for any of the recipes in your {recipes_box.name}')
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
        return function(*args)
                    
    return inner_function

def archive_shopping_list(function):
    
    def inner_function (*args):
        shopping_list_archive.append(function(*args))
        print ('List was archived')
        return function
    return inner_function 

@archive_shopping_list
@pretty_print_recipe
def prepare_shopping_list(fridge, recipe):
    shopping_list = {}
    for ingredient, quantity in recipe.items():
        if ingredient in fridge:
            if fridge[ingredient]<quantity:
                shopping_list[ingredient]=quantity-fridge[ingredient]
        else:
            shopping_list[ingredient]=quantity
    return shopping_list


            
    




