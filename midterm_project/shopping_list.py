# class instantiate each recipe
class Recipe(PrettyPrinterMixin):

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

    # method get a recipe as argument, extract the recipe from recipes_box and print it
    def pick(self, recipe=None):
        if recipe:
            index = self._recipesbox_list.index(recipe)
        else:
            max_rand_no = len(self._recipesbox_list)
            index = randrange(0, max_rand_no, 1)

        return self._recipesbox_list[index]