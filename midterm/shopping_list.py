from pprint import pprint
import random
import sys

class PrittyPrinterMixin:

    # def box_it(fnc):
        
    #     def inner_func(self):
    #         print('********************')
    #         fnc(self)
    #         print('********************')
    #     return inner_func
    
    
    # @box_it
    def __str__(self):
        
        if hasattr(self, 'ingredients'):
            print_view = f'*************************'
            print_view += '\n'
            print_view += f'{self.get_name()}'
            print_view += '\n'
            print_view += f'************************'
            print_view += '\n'
            for index, (ingredient,quantity) in enumerate(self.ingredients.items(), start=1):
                print_view += f'{index}. {ingredient}: {quantity}' + '\n'
            print_view += '\n'
            print_view += f'************************'
            return (print_view)
        else:
            print_view = f'*************************'
            print_view += '\n'
            print_view += f'Fridge contains:'
            print_view += '\n'
            print_view += f'************************'
            print_view += '\n'
            for index, (ingredient,quantity) in enumerate(self.fridge_list.items(), start=1):
                print_view += f'{index}. {ingredient}: {quantity}' + '\n'
            print_view += '\n'
            print_view += f'************************'
            return (print_view)
 


class Recipe(PrittyPrinterMixin):

    def __init__(self, recipe_name, ingredients):
        
        self._recipe_name = recipe_name
        self._ingredients = ingredients
    
    @property
    def recipe_name(self):
        return self._recipe_name

    @property
    def ingredients(self):
        return self._ingredients

    def __str__(self):
        return super().__str__()

    def get_name(self):
        return self.recipe_name

    def __len__(self):
        return len(self.ingredients)

    def __getitem__(self, index):
        return self.ingredients[index]

    def keys(self):
        return self.ingredients.keys()

    def __contains__(self, item):
        return item in self.ingredients.keys()

    def __iter__(self):
        return iter(self.ingredients)

    def values(self):
        return self.ingredients.values()

    def items(self):
        return self.ingredients.items()

    

class RecipeBox:

    def __init__(self):
        self.recipebox = {}

    def __getitem__(self, index):
        return self.recipebox[index]

    def __setitem__(self, index, newrecipe):
        self.recipebox[index] = newrecipe

    def __delitem__(self, recipe):
        del self.recipebox[recipe]

    def __len__(self):
        return len(self.recipebox)

    # def insert(self, recipe,index):
    #     self.recipebox.insert(index,recipe)

    def pop(self, recipe=None):
        if recipe:
            self.recipebox.pop(recipe)
        else:
            self.recipebox.pop()

    def __contains__(self,recipe):
        return recipe in self.recipebox

    # def remove(self, recipe):
    #     self.recipebox.remove(recipe)

    def add_recipe(self,recipe):
        self.recipebox[recipe.recipe_name] = recipe.ingredients

    def remove_recipe(self,recipe):
        del self.recipebox[recipe.recipe_name]
    
    def pick(self, recipe=None):
        if recipe:
            print (f' Selected recipe is: {recipe.recipe_name}, and contains: {recipe.ingredients}')
        else:
            random_recipe = random.choice(list(self.recipebox.keys()))
            print (f' Random recipe is: {random_recipe} and contains: {self.recipebox[random_recipe]}')

    def __str__(self):
        return (f'Recipebox contains: {list(self.recipebox.keys())}')

    def values(self):
        return self.recipebox.values()

    def keys(self):
        return self.recipebox.keys()

    def items(self):
        return self.recipebox.items()


class Fridge(PrittyPrinterMixin):

    def __init__(self):
        self.fridge_list = {}

    
    def get_name(self):
        return self.fridge_list

    def __getitem__(self,index):
        return self.fridge_list[index]

    def __setitem__(self,item,new_quantity):
        self.fridge_list[item] = new_quantity

    def __delitem__(self,item):
        del self.fridge_list[item]

    def __iter__(self):
        return iter(self.fridge_list)

    def __len__(self):
        return len(self.fridge_list)

    def keys(self):
        return self.fridge_list.keys()

    def items(self):
        return self.fridge_list.items()
    
    def values(self):
        return self.fridge_list.values()
    
    def __contains__(self,item):
        return item in self.fridge_list

    def add_food(self,item,quantity):
        self.fridge_list[item] = quantity
        print(f'{item} added to fridge with {quantity} piece(s).')

    def remove_food(self,item):
        del self.fridge_list[item]
        print(f'{item} was removed from the fridge.')

    def update_to_food(self,item,quantity):
        if item in self.fridge_list:
            self.fridge_list[item] += quantity
            print(f'The {item} was updated with {quantity} pieces.')
        else:
            print(f'The {item} is not in the fridge, cannot update.')

    def remove_from_food(self,item,quantity):
        if item not in self.fridge_list:
            print(f'The {item} is not in the fridge. Cannot take out from it.')
        else:
            self.fridge_list[item] -= quantity
            if self.fridge_list[item] == 0:
                del self.fridge_list[item]
                print(f'You took out all the {item}. Go and shop some more.')
            else:
                print(f'We took out {quantity} piece(s) from the {item}.')


    def __str__(self):
        return super().__str__()

    def check_recipe(self,recipe):

        have_in_fridge = []
        not_in_fridge = []
        for item in recipe.ingredients.keys():
            if item in self.fridge_list.keys():
                have_in_fridge.append(item)
            else:
                not_in_fridge.append(item)
                

        print(f'Things for preparing {recipe.recipe_name} we don\'t have in the fridge: {not_in_fridge}')
        print(f'Things for preparing {recipe.recipe_name} we have in the fridge: {have_in_fridge}')


def check_the_fridge(fridge, recipe_list):

    preparable_recipes = []
    for name, ingredients in recipe_list.items():
        count_recipe_ingredient = 0
        for ingredient in ingredients.keys():
            if ingredient in fridge:
                count_recipe_ingredient += 1
                if count_recipe_ingredient / len(recipe_list.values()) >= 0.5:
                    preparable_recipes.append(name)

    return f'Recipes we can make from the fridge: {preparable_recipes}'


#shop={}
def pretty_print_recipe(shop_display):
    def wrapper1(*args):
        shopping_list_arc=shop_display(*args)   #ramane
        for key,value in shopping_list_arc:
            #for k, v in key,value:
            printer=f'{key}:{value}\n'
        art_ascii = r"""
   ______________________________
 / \                             \.
|   |                            |.
 \_ |                            |.
    |                            |.
    |                            |.
    |                            |.
    |                            |.
    |                            |.
    |                            |.
    |                            |.
    |                            |.
    |                            |.
    |                            |.
    |                            |.
    |   _________________________|___
    |  /                            /.
    \_/dc__________________________/.
            """
        return printer+art_ascii
    return wrapper1



shopping_list_archive = []
def archive_shopping_list(shop_ing):
    def wrapper(*args):
        shopping_list_archive.append(shop_ing(*args))
        print (f'The {shop_ing(*args)} items were included in archive')
        return shopping_list_archive 
    return wrapper

@archive_shopping_list
#@pretty_print_recipe
def prepare_shopping_list(recipe,fridge):
    shopping_list = {}
    for recipe_ingredient, recipe_quantity in recipe.items():
        if recipe_ingredient not in fridge:
            shopping_list[recipe_ingredient] = recipe_quantity
        elif recipe_quantity>fridge[recipe_ingredient]:
            shopping_list[recipe_ingredient] = recipe_quantity - fridge[recipe_ingredient]
    return shopping_list