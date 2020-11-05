from muffin_man_shopping_list import Recipe, RecipesBox, Fridge, PrettyPrinterMixin, check_the_fridge, \
    pretty_print_recipe, archive_shopping_list, prepare_shopping_list, shopping_archive

mac_and_cheese_ingredients = {'macaroni': 2, 'cheese': 2, 'oil': 2, 'salt': 2}
croque_monsieur_ingredients = {'bread': 10, 'cheese': 5, 'ham': 5, 'butter': 1}
pasta_pesto_ingredients = {'pasta': 2, 'pesto': 2, 'nuts': 1, 'oil': 3, 'basil': 5, 'garlic': 3}
stuffed_peppers_ingredients = {'peppers': 8, 'minced meat': 10, 'rice': 5, 'onion': 1}
tiramisu_ingredients = {'lady fingers': 40, 'mascarpone': 2, 'eggs': 6, 'cream': 1, 'coffee': 4, 'cocoa': 1}
chocolate_cake_ingredients = {'flour': 10, 'eggs': 5, 'sugar': 2, 'chocolate': 4, 'milk': 2}

mac_and_cheese = Recipe('Mac and Cheese', mac_and_cheese_ingredients)
croque_monsieur = Recipe('Croque Monsieur', croque_monsieur_ingredients)
pasta_pesto = Recipe('Pasta with Pesto', pasta_pesto_ingredients)
stuffed_peppers = Recipe('Stuffed Peppers', stuffed_peppers_ingredients)
tiramisu = Recipe('Tiramisu', tiramisu_ingredients)
chocolate_cake = Recipe('Chocolate Cake', chocolate_cake_ingredients)

print(pasta_pesto)
print(mac_and_cheese)
print(croque_monsieur)
print(chocolate_cake)
print(tiramisu)
print(stuffed_peppers)

# chocolate_cake.name = 'Banana bread'
# stuffed_peppers.ingredients = {'tomatoes': 4, 'onions': 5, 'zucchini': 3}

recipes_box = RecipesBox()

recipes_box.add_recipe(croque_monsieur)
recipes_box.add_recipe(mac_and_cheese)
recipes_box.add_recipe(pasta_pesto)
recipes_box.add_recipe(stuffed_peppers)
recipes_box.add_recipe(pasta_pesto)
print(recipes_box, '\n')

recipes_box.delete_recipe(pasta_pesto)
recipes_box.delete_recipe(stuffed_peppers)
recipes_box.delete_recipe(stuffed_peppers)
print(recipes_box, '\n')

recipes_box.pick_recipe(mac_and_cheese)
recipes_box.pick_recipe(tiramisu)
recipes_box.pick_recipe()

muffin_man_fridge = Fridge()
print(muffin_man_fridge, '\n')

muffin_man_fridge.add_item('Eggs', 30)
muffin_man_fridge.add_item('Tomatoes', 50)
muffin_man_fridge.add_item('Juice', 4)
muffin_man_fridge.add_item('Cheese', 40)
muffin_man_fridge.add_item('Pesto', 4)
muffin_man_fridge.add_item('Pesto', 10)
muffin_man_fridge.add_item('Mascarpone', 50)
muffin_man_fridge.add_item('Chocolate', 10)
print(muffin_man_fridge, '\n')

muffin_man_fridge.delete_item('Eggs')
muffin_man_fridge.delete_item('Cheese')
muffin_man_fridge.delete_item('Cheese')
print(muffin_man_fridge, '\n')

muffin_man_fridge.remove_quantity_item('Juice', 10)
muffin_man_fridge.remove_quantity_item('Apples', 13)
muffin_man_fridge.remove_quantity_item('Tomatoes', 10)
muffin_man_fridge.remove_quantity_item('Tomatoes', 40)
print(muffin_man_fridge, '\n')

muffin_man_fridge.add_quantity_item('Cheese', 30)
muffin_man_fridge.add_quantity_item('Halloumi', 50)
muffin_man_fridge.add_quantity_item('Veggie Burger', 4)
muffin_man_fridge.add_quantity_item('Ham', 10)
muffin_man_fridge.add_quantity_item('Ham', 20)
muffin_man_fridge.add_quantity_item('Bread', 20)
print(muffin_man_fridge, '\n')

print(muffin_man_fridge.check_recipe(mac_and_cheese))
print(muffin_man_fridge.check_recipe(croque_monsieur))
print(muffin_man_fridge.check_recipe(tiramisu))

if 'Juice' in muffin_man_fridge:
    print('YES! In Muffin Man Fridge')
else:
    print('Not in Muffin Man Fridge!')

if 'Candy' in muffin_man_fridge:
    print('YES! In Muffin Man Fridge')
else:
    print('Not in Muffin Man Fridge!')

print(muffin_man_fridge, '\n')
print(len(muffin_man_fridge))
del muffin_man_fridge['Juice']
muffin_man_fridge.add_item('Pasta', 10)
muffin_man_fridge.add_item('Nuts', 10)
muffin_man_fridge.add_item('Oil', 10)
muffin_man_fridge.add_item('Basil', 10)
muffin_man_fridge.add_item('Garlic', 10)
print(muffin_man_fridge, '\n')

recipes_box.add_recipe(croque_monsieur)
recipes_box.add_recipe(mac_and_cheese)
recipes_box.add_recipe(pasta_pesto)
recipes_box.add_recipe(stuffed_peppers)
recipes_box.add_recipe(pasta_pesto)
print(recipes_box, '\n')

print(check_the_fridge(muffin_man_fridge, recipes_box))

muffin_man_fridge.pretty_print()
mac_and_cheese.pretty_print()
tiramisu.pretty_print()
chocolate_cake.pretty_print()

print(muffin_man_fridge, '\n')
prepare_shopping_list(muffin_man_fridge, mac_and_cheese)
prepare_shopping_list(muffin_man_fridge, pasta_pesto)
prepare_shopping_list(muffin_man_fridge, croque_monsieur)
prepare_shopping_list(muffin_man_fridge, stuffed_peppers)

print('This is the Shopping Archive:', shopping_archive)
