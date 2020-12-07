import random

class PrettyPrinter:
    
    def __str__(self):
        star_line = '*' * (len(self.name) + 4) + '\n'
        string = f'{star_line} \n {self.name} \n {star_line} \n'     
        for index, (keys, values) in enumerate(self.items(), 1):
            string += f'{index}. {keys}: {values} \n'
        string += f'\n {star_line}'
        return (string)
  
class Recipe(PrettyPrinter):
    
    def __init__(self, name, dictionary_of_ingredients):
        list_of_ingredients = []
        self._name = name
        for ingredient, quantity in dictionary_of_ingredients.items():
            list_of_ingredients.append((ingredient, quantity))
        self.tuple_of_ingredients = tuple(list_of_ingredients)
    
    @property
    def name(self):
        return self._name
    
    def __getitem__(self, index):
        return self.tuple_of_ingredients[index]
    
    def __contains__(self, ingredient, quantity):
        if (ingredient, quantity) in self.tuple_of_ingredients:
            return True
        else:
            return False
        
    def get(self, index):
        return self.tuple_of_ingredients[index]
    
    def __eq__(self, other):
        if isinstance(other, Recipe):
            return self.tuple_of_ingredients == other.tuple_of_ingredients
        return False
    
    def __ne__(self, other):
        return not self.__eq__(other)
       
    def __iter__(self):
        return iter(self.tuple_of_ingredients)       
        
    def __len__(self):
        return len(self.tuple_of_ingredients)

    def dict_from_tuple(self):
        dictionary_of_ingredients = {}
        for (ingredient, quantity) in self.tuple_of_ingredients:
            dictionary_of_ingredients[ingredient] = quantity
        return dictionary_of_ingredients
    
    def items(self):
        return self.dict_from_tuple().items()
    
    def keys(self):
        return self.dict_from_tuple().keys()
    
    def values(self):
        return self.dict_from_tuple().values()
       
    def __str__(self):
        return super().__str__()
                    
class RecipesBox():
   
    def __init__(self, name, recipes_list):
        self.name = name
        self.recipes_list = recipes_list
    
    def __iter__(self):
        return iter(self.recipes_list)
    
    def insert(self, index, recipe):
        return self.recipes_list.insert(index, recipe)
    
    def __getitem__(self, index):
        return self.recipes_list[index]
    
    def __setitem__(self, index, value):
        self.recipes_list[index]=value
    
    def __delitem__(self, index):
        del self.recipes_list[index]
        
    def __len__(self):
        return len(self.recipes_list)
    
    def pick(self, recipe_to_extract=None):
        if recipe_to_extract:
            for recipe in self.recipes_list:
                if recipe.name == recipe_to_extract:
                    return recipe
        else:
            return random.choice(self.recipes_list)
    
    def add(self, recipe_to_add):
        self.recipes_list.append(recipe_to_add)
    
    def delete(self, recipe_to_delete):
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
        
    def add(self, product_name, product_quantity):
        if product_name not in self.dictionary_of_products:
            self.dictionary_of_products[product_name] = product_quantity
        self.dictionary_of_products[product_name] += product_quantity
               
    def extract(self, product_name, product_quantity):
        if product_name in self.dictionary_of_products:
            self.dictionary_of_products[product_name] -= product_quantity
            if self.dictionary_of_products[product_name] == 0:
                del self.dictionary_of_products[product_name]
                print (f'Product {product_name} removed from the fridge')              
            elif self.dictionary_of_products[product_name] < 0:
                del self.dictionary_of_products[product_name]
                print (f'The quantity of {product_name} in the fridge is insufficient for your recipe, buy some more')               
            else:
                print(f'The quantity of {product_name} left in the fridge after extraction is {self.dictionary_of_products[product_name]}')
        else:
            print (f'Ingredient not in fridge, go to the shop to buy {product_name}')
                    
    def check_recipe(self, recipe):
        recipe_ingredients = set(recipe.keys())
        fridge_ingredients = set(self.dictionary_of_products.keys())
        available_ingredients = list(recipe_ingredients & fridge_ingredients)
        ingredients_to_be_bought = list(recipe_ingredients.difference(fridge_ingredients))
        print (f'For the {recipe.name}, ingredients to be bought are {ingredients_to_be_bought} and available ingredients are {available_ingredients}')
        return (ingredients_to_be_bought, available_ingredients)
    
    def __str__(self):
        return super().__str__()       

def check_the_fridge(fridge, recipes_box):
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
                space_string = ' '*space_count
                string_to_print += f'{current_line}{space_string}| |\n'
            string_to_print += r'''| |___________________________________________________________| |
|_______________________________________________________________|
                   )__________|__|__________(
                  |            ||            |
                  |____________||____________|
                    ),-----.(      ),-----.(
                  ,'   ==.   \    /  .==    `.
                 /            )  (            \
                 `==========='    `===========' '''
            print(string_to_print)
        else:
            print("The shopping list is empty")
        return function(*args)
                    
    return inner_function

def archive_shopping_list(function):
    
    def inner_function(*args):
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
    




