from random import randint

class Recipe:

    # is_initialized is a bool that keeps track of whether or not the object has been given values so we can raise an error if the user tries updating them
    is_initialized = False

    def __init__(self, name, ingredients):
        # Name is a string
        self.name = name

        # Ingredients is a dictionary containing ingredients as keys and quantities as values
        self.ingredients = ingredients if ingredients else {}

    def __str__(self):
        # number_of_stars is calculated based on name length every time so it looks appropriate for any name
        number_of_stars = len(self.name) + 3

        # this line of code assigns to the variable pretty_string the name of the recipe surrounded by stars. '\n' is newline
        pretty_string = '*' * number_of_stars + '\n' + self.name + '\n' + '*' * number_of_stars + '\n'

        # for loop adds the ingredients to the string using the join() method, which is called off of a separator (in this case '\n')
        # and takes a tuple as an argument that is going to be joined
        for index, (key, value) in enumerate(self.ingredients.items(), start = 1):
            pretty_string = '\n'.join((pretty_string, f'{index}. {key.title()}: {value}'))
        
        # finally, the last newlines and stars are added and the variable pretty_string is returned
        pretty_string = pretty_string + '\n' * 2 + '*' * number_of_stars
        return pretty_string
    
    # getitem effectively transforms the object in a list of dictionaries
    def __getitem__(self, given_index):
        for index, (key, value) in enumerate(self.ingredients.items(), start = 1):
            if given_index == index:
                return {key: value}
    
    # adds len() functionality
    def __len__(self):
        return len(self.ingredients)

    # makes the object iterable
    def __iter__(self):
        return iter(self.ingredients)

    # implement .keys() functionality
    def keys(self):
        return self.ingredients.keys()
    
    # stop the user from updating the name attribute
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if self.is_initialized:
            raise NameError("You can't update the recipe!")
        self._name = name
    
    # stop the user from updating the ingredients attribute
    @property
    def ingredients(self):
        return self._ingredients

    @ingredients.setter
    def ingredients(self, ingredients):
        if self.is_initialized:
            raise NameError("You can't update the recipe!")
        self._ingredients = ingredients
        # is_initialized is only updated in the ingredients setter because it is the last thing to get initialized
        self.is_initialized = True

class RecipesBox():

    # recipe_list is a list that will contain all of the recipe objects
    recipe_list = list()

    # the init function handles an unknown number of recipes given to the RecipesBox object
    def __init__(self, *recipes):
        for recipe in recipes:
            self.recipe_list.append(recipe)
    
    def __str__(self):
        # string_list will hold the names of the recipes
        string_list = ""

        # add the names of the recipes to string_list and add a newline as long as there are more recipe names to be added
        for index, recipe in enumerate(self.recipe_list):
            string_list = string_list + recipe.name
            if index != len(self.recipe_list)-1:
                string_list += '\n'

        return string_list
    
    # add_recipe adds a recipe
    def add_recipe(self, new_recipe):
        self.recipe_list.append(new_recipe)
    
    # remove_recipe removes a recipe
    def remove_recipe(self, recipe):
        self.recipe_list.remove(recipe)
    
    # pick function randomly selects a recipe or returns a recipe if it is given a name
    def pick(self, name=None):
        if name == None:
            random_number = randint(0, len(self.recipe_list)-1)
            return self.recipe_list[random_number]
        else:
            for recipe in self.recipe_list:
                if recipe.name == name:
                    return recipe

          
class PrettyPrinter:

    def __str__(self):
        if hasattr(self, 'ingredients'):
            pretty_recipe_string = r'''
  _______________________________
 / \                             \
|   |                            |
 \_ |                            | '''

            pretty_name_string = '\n    |      ' + self.name  # pylint: disable=maybe-no-member

            nstr_len = len(pretty_name_string)

            pretty_recipe_string += pretty_name_string + ' ' * (34 - nstr_len) + '|'

            pretty_recipe_string += '\n    |                            |'

            for index, (key, value) in enumerate(self.ingredients.items(), start = 1):  # pylint: disable=maybe-no-member
                pretty_ingredient_string = '\n    |    ' + str(index) + '. ' + key.title() + ': ' + str(value)
                istr_len = len(pretty_ingredient_string)
                pretty_recipe_string += pretty_ingredient_string + ' ' * (34 - istr_len) + '|'
            
            pretty_recipe_string += r'''
    |   _________________________|___
    |  /                            /
    \_/____________________________/ '''
            return pretty_recipe_string                          

class RecipePrinter(PrettyPrinter, Recipe):
    pass

mac_and_cheese_ingredients = {
    'macaroni': 1,
    'cheese': 0.5,
    'pesto': 1
}

mac_and_cheese = Recipe(
    "Famous Mac & Cheese",
    mac_and_cheese_ingredients
)

mac_and_cheese_ingredients2 = {
    'macaroni': 1,
    'cheese': 0.5
}

mac_and_cheese2 = Recipe(
    "Famous Mac & Cheese2",
    mac_and_cheese_ingredients2
)

# printrecipe = RecipePrinter("Muffin Man & Cheese", mac_and_cheese_ingredients)
# print(printrecipe)
# print(mac_and_cheese)
# ingredients = list(mac_and_cheese.keys())
# print(ingredients)
# print(mac_and_cheese[1])
# for ingredient in mac_and_cheese:
#     print(ingredient)
# print(len(mac_and_cheese))

# box = RecipesBox(mac_and_cheese, mac_and_cheese2)
# print(box)
# print(box.pick())


