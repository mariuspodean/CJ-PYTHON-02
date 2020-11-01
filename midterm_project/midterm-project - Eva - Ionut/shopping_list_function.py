
def prepare_shopping_list(fridge, recipe):
    products_fridge = {item.lower(): fridge[item] for item in fridge}
    print(products_fridge)

    products_recipe = dict(recipe.ingredients.items())
    print(products_recipe)

    shopping_list = {}

    for product, quantity in products_recipe.items():
        if product not in products_fridge:
            shopping_list[product] = quantity
        else:
            if quantity > products_recipe[product]:
                shopping_list[product] = quantity - products_recipe[product]
            break

    return f'This is the needed shopping list for {recipe.name}: {shopping_list}'