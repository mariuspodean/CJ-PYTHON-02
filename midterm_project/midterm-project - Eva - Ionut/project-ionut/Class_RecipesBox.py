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