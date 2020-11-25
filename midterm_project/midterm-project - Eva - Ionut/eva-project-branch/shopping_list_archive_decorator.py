
shopping_archive = []


def archive_shopping_list(shop_list):

    def archive_store(*args):
        if shop_list(*args):
            shopping_archive.append(shop_list(*args))
            print(f'Added {shop_list(*args)} to the Shopping Archive')
        else:
            print(f'No shopping list to add to archive')
    return archive_store


@archive_shopping_list
def prepare_shopping_list(fridge, recipe):
    products_fridge = {item.lower(): fridge[item] for item in fridge}

    shopping_list = {}

    for product, quantity in recipe.ingredients.items():
        if product not in products_fridge:
            shopping_list[product] = quantity
        else:
            if quantity > products_fridge[product]:
                shopping_list[product] = quantity - products_fridge[product]

    return shopping_list
