from random import randrange
import time

shopping_list_archive=[]

class Recipe:

    def __init__(self, recipe_name=None, recipe_ingredients=None):
        self.recipe_name = recipe_name
        self.recipe_ingredients = recipe_ingredients

    def __repr__(self):
        print_string = f'{self.recipe_name}: {self.recipe_ingredients}'
        return print_string

    def __len__(self):
        return len(self.recipe_ingredients)

    def __iter__(self):
        return self.recipe_ingredients

    def __getitem__(self, item):
        return self.recipe_ingredients[item]

    def __contains__(self, item):
        return item in self.recipe_ingredients

    def keys(self):
        return self.recipe_ingredients.keys()

    def values(self):
        return self.recipe_ingredients.values()

    def items(self):
        return self.recipe_ingredients.items()


# class instantiate a recipe_box instance for archive all the recipes created
class RecipesBox:

    def __init__(self):
        self._recipesbox_list = []

    def __str__(self):
        print_string = ''
        for recipe in self._recipesbox_list:
            recipe_title = f'{recipe.recipe_name}\n'
            print_string = ''.join((print_string, recipe_title))
        return print_string

    def __len__(self):
        return len(self._recipesbox_list)

    def __getitem__(self, index):
        return self._recipesbox_list[index]

    def __contains__(self, item):
        return item in self._recipesbox_list

    def __setitem__(self, index, value):
        self._recipesbox_list[index] = value

    def __delitem__(self, index):
        del self._recipesbox_list[index]

    def remove(self, item):
        self._recipesbox_list.remove(item)

    def append(self, item):
        self._recipesbox_list.append(item)

    # eliminate a recipe from recipes_box list by its index
    def pop(self, index=None):
        if index:
            return self._recipesbox_list.pop(index)
        else:
            return self._recipesbox_list.pop()

    # method get a recipe as argument, extract the recipe from recipes_box and print it #?Ionut: aici nu e nici un print
    def pick(self, recipe=None):
        if recipe:
            index = self._recipesbox_list.index(recipe)
        else:
            max_rand_no = len(self._recipesbox_list)
            index = randrange(0, max_rand_no, 1) #?Ionut: aici nu pare a functiona

        return self._recipesbox_list[index]

class Fridge:
    
    def __init__(self,name=None, inside_fridge=None):
        self.inside_fridge = inside_fridge
        self.name = name
       
# When printing the fridge object, it will print similar to a recipe, its contents.
    def __str__(self):
        print_content = ''
        for ingredient in self.inside_fridge:
            print_content = ' '.join((print_content, ingredient, str(self.inside_fridge[ingredient]))) 
            #mai sus nu inteleg de ce dupa join trebuie doua paranteze
            print_content = f'{print_content}\n'
        return print_content

# de aici in jos tot ce e cu __ urmareste sa faca mutable mapping
    def __contains__(self, ingredient):
        return ingredient in self.inside_fridge

# We can also ask if a certain product is in the fridge
    def check_ingredient(self, ingredient):
        if ingredient in self.inside_fridge:
            print ('Yap')
    
    def __iter__(self):
        return iter(self.inside_fridge)

    def __len__(self):
        return len(self.inside_fridge)

    def __getitem__(self, ingredient):
        return self.inside_fridge[ingredient]

    def __setitem__(self, ingredient, quantity):
        self.inside_fridge[ingredient] = quantity

    def __delitem__(self, ingredient):
        del self.inside_fridge[ingredient]

# We can add new items in the fridge. Tot aici actualizam cantitatile in plus.
    def add_ingredient_in_fridge(self, ingredient, quantity):
        if ingredient in self.inside_fridge:
            self.inside_fridge[ingredient] += quantity
        else:
            self.inside_fridge[ingredient] = quantity

# We can [...] remove existing ones. Tot aici actualizam cantitatile in minus. Anuntam cand ramanem fara ceva in frigider.
    def remove_ingredient_from_fridge(self, ingredient, quantity):
        if ingredient in self.inside_fridge:
            self.inside_fridge[ingredient] = self.inside_fridge[ingredient] - quantity
            if self.inside_fridge[ingredient] <= 0:
                print (f'No more {ingredient} in the fridge.')
                del self.inside_fridge[ingredient]
        else:
            print ('No such ingredient in the fridge')
    
    def check_recipe (self,recipe)->[]: #cu litera mare sau mica, recipe?
        list_we_have = []
        list_to_shop = []
        for ingredient in recipe.keys():
            if ingredient in self:
                if self[ingredient] >= recipe[ingredient]:
                    list_we_have.append(ingredient)
                else:
                    quantity_to_buy = recipe[ingredient] - self[ingredient]
                    list_to_shop.append((ingredient, quantity_to_buy))
            else:
                list_to_shop.append((ingredient,recipe[ingredient]))
        print (f'We already have: {list_we_have}')
        print (f'We need to buy: {list_to_shop}')
        return list_to_shop

    def update(self,ingredients):
        if(self.inside_fridge is None):
            self.inside_fridge = {}
        for ingredient in ingredients.items():
            (name,quantity)= ingredient
            self.inside_fridge[name]= quantity
    
    def update_quantity(self,ingredient,quantity):
        pass
                

class PrettyPrinter():

    def __init__(self,name=None,ingredients=None):
        self.name = name
        self.ingredients = ingredients
        
        super().__init__(name,ingredients)
    
    def pretty_print(self):
        header = ''' 
_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._
 ,'_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._`.'''
        footer = '''
( (_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._) )
 `._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._,'''
        spacer = '''
 ) )                                                       ( ('''
        to_print=header
        if(self.name):
            to_print+= self.__replace_line__(self.name) + spacer
        else:
            to_print+= self.__replace_line__('Our Fridge') + spacer
        for ingredient in self.ingredients.items():
            (key,value) = ingredient
            replace_with = key + ' : '+ str(value)
            to_print += self.__replace_line__(replace_with) + spacer
        to_print+=footer
        print(to_print)

    def __replace_line__(self,replace_with):
        filler ='''
( (                                                         ) )'''
        to_replace = len(replace_with)*' '
        return filler.replace(to_replace,replace_with,1)



class PrettyRecipe(PrettyPrinter,Recipe):
    pass


class PrettyFridge(PrettyPrinter,Fridge):
    pass

def check_the_fridge(fridge, recipes):
    half_or_more_ingredients_recipies = []
    less_than_half_ingredients_recipies = []
    for recipe in recipes:
        available_ingredients = 0
        for ingredient in recipe.keys():
            if ingredient in fridge:
                available_ingredients += 1
        if available_ingredients >= (len(recipe.keys())/2):
            half_or_more_ingredients_recipies.append(recipe.recipe_name)
        else:
            less_than_half_ingredients_recipies.append(recipe.recipe_name)
    print(f'We have half or more ingredients for: {half_or_more_ingredients_recipies}')
    print(f'We have less than half ingredients for: {less_than_half_ingredients_recipies}')
    return half_or_more_ingredients_recipies           

# check_the_fridge(our_fridge, our_recipes_box)

def pretty_print_recipe(function):

    def wrapper(fridge,recipe):
        shopping_list=function(fridge,recipe)
        missing_items = PrettyRecipe("Shopping List:",shopping_list)
        missing_items.pretty_print()
        return shopping_list

    return wrapper

def archive_shopping_list(fnc2):
    def inner_func_2(fridge, recipe):
        shopping_list = fnc2(fridge, recipe)
        time_now = time.localtime()
        date_today = time.strftime('%d %m %Y', time_now)

        if type(shopping_list) == dict:
            shopping_list_archive.append((date_today, recipe.recipe_name, shopping_list))

        return shopping_list

    return inner_func_2

@archive_shopping_list
@pretty_print_recipe
def prepare_shopping_list(fridge, recipe):
    shopping_list = {}
    for ingredient in recipe.keys():
        if ingredient in fridge:
            if fridge[ingredient] <= recipe[ingredient]:
                quantity_to_buy = recipe[ingredient] - fridge[ingredient]
                shopping_list.update({ingredient: quantity_to_buy})
    print (f'Shopping list: {shopping_list}')
    return shopping_list
