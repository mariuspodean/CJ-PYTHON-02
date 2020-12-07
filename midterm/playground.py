import shopping_list
from shopping_list import PrittyPrinterMixin, Recipe, RecipeBox, Fridge, check_the_fridge, archive_shopping_list, prepare_shopping_list

canibale_pizza_ingredients = {'salami': 2, 'cheese': 3, 'pizzabase': 1, 'ham':2}
ham_and_eggs_ingredients = {'ham': 2, 'eggs': 4, 'oil':1, 'salt':1}
mac_and_cheese_ingredients = {'macaroni': 5, 'cheese': 3, 'salt': 1, 'tomato':2}
salad_ingredients = {'cucumber': 4, 'eggs': 3, 'salad':2, 'olive':2}
vegetable_soup_ingredients = {'ham':1, 'tomato':1, 'potato':2, 'oil':1, 'carrot':2}



canibale_pizza = Recipe('Canibale Pizza', canibale_pizza_ingredients)
ham_and_eggs = Recipe('Ham and eggs', ham_and_eggs_ingredients)
mac_and_cheese = Recipe("Famous Mac & Cheese", mac_and_cheese_ingredients)
salad = Recipe('Caesar salad', salad_ingredients)
vegetable_soup = Recipe('Vegetable Soup', vegetable_soup_ingredients)



print('salt' in mac_and_cheese)
print('olive' in mac_and_cheese)

print(mac_and_cheese)
print(ham_and_eggs)
print(vegetable_soup)

recipelist = RecipeBox()
recipelist.add_recipe(mac_and_cheese)
recipelist.add_recipe(ham_and_eggs)
recipelist.add_recipe(canibale_pizza)
recipelist.add_recipe(salad)
recipelist.add_recipe(vegetable_soup)

print(recipelist)
# print(recipelist.values())
recipelist.remove_recipe(mac_and_cheese)
print(recipelist)

recipelist.pick()
recipelist.pick(mac_and_cheese)

fridge = Fridge()
fridge.add_food('macaroni',3)
fridge.add_food('bread',2)
fridge.add_food('salt', 2)
fridge.add_food('ham', 3)
fridge.add_food('eggs', 4)
fridge.add_food('tomato', 2)
fridge.add_food('ananas', 3)

print(fridge)

fridge.update_to_food('milk', 8)
fridge.update_to_food('bread', 3)
print(fridge)
print('macaroni' in fridge)

fridge.remove_from_food('bread', 1)
fridge.remove_from_food('ananas',3)
print(fridge)

fridge.remove_food('bread')
print(fridge)


fridge.check_recipe(mac_and_cheese)
print(check_the_fridge(fridge,recipelist))

print(prepare_shopping_list(mac_and_cheese,fridge))
print(prepare_shopping_list(canibale_pizza,fridge))
print(prepare_shopping_list(salad,fridge))

print(shopping_list.shopping_list_archive)