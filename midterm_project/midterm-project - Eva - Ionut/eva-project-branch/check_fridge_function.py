
def check_the_fridge(fridge, recipe_box):
    contents_fridge = set([item.lower() for item in fridge])
    print('Fridge', contents_fridge)

    list_ingredients_for_recipe = {recipe: set(recipe_box[recipe].keys()) for recipe in recipe_box}
    print('Ingredients for recipe:', list_ingredients_for_recipe)

    possible_recipes = []

    for name, ingredients in list_ingredients_for_recipe.items():
        if len(ingredients.intersection(contents_fridge)) >= len(ingredients)/2:
            possible_recipes.append(name)

    return f'Possible recipes you can make with the products in your fridge:{(list(possible_recipes))}'