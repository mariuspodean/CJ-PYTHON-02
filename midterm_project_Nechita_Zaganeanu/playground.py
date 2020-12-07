from shopping_list import Recipe, RecipesBox, Fridge, check_the_fridge, prepare_shopping_list, shopping_list_archive
from collections.abc import MutableSequence, Mapping, MutableMapping

chicken_soup_ingredients = {
    'chicken': 1,
    'carrots': 2,
    'onion': 1,
    'noodles': 15,
    'parsely': 0.5
}

choccolate_cake_ingredients = {
    'flour': 700,
    'eggs': 5,
    'milk': 1,
    'maple syrup': 150,
    'cocoa': 300,
    'butter': 2
}

scrumbled_eggs_ingredients = {
    'eggs': 4,
    'mushrooms': 6,
    'red onion': 1,
    'olive oil': 20,
    'cheese': 100
}

pork_steak_ingredients = {
    'pork muscle': 1000,
    'olive oil': 200,
    'bell pepper': 2,
    'garlic': 5,
    'oranges': 2,
    'cabbage': 1
}

pancakes_ingredients = {
    'flour': 500,
    'milk': 500,
    'sparkling water': 250,
    'egg': 2,
    'agave syrup': 100
}

mac_and_cheese_ingredients = {
    'macaroni': 1,
    'cheese': 0.5
}

dictionary_of_products = {
    'milk':1,
    'eggs':3,
    'cheese':1,
    'butter':1,
    'jam':1,
    'olives':23,
    'tomatoes':7,
    'carrots':2
}

chicken_soup = Recipe('Grandma\'s chicken soup', chicken_soup_ingredients)
choccolate_cake = Recipe('Delicious Choccolate Cake', choccolate_cake_ingredients)
scrumbled_eggs = Recipe('Scrumbled Eggs', scrumbled_eggs_ingredients)
pork_steak = Recipe('Mediteranean Pork Steak', pork_steak_ingredients)
pancakes = Recipe('Simple Pancakes', pancakes_ingredients)
mac_and_cheese = Recipe('Famous Mac & Cheese', mac_and_cheese_ingredients)

print (choccolate_cake)

ingredients=list(pancakes.keys())
print('Lista de ingrediente pentru pancakes este: ', ingredients, '\n')

# print(pork_steak.name)
# pork_steak.name = 'Maciupiciu'
# pork_steak.dictionary_of_ingredients['pepper'] = 2
# print(pork_steak.dictionary_of_ingredients)

recipes_box = RecipesBox('Alexandra\'s list', [chicken_soup, choccolate_cake, scrumbled_eggs, mac_and_cheese])

recipes_box.add(pork_steak)
recipes_box.add(pancakes)
recipes_box.delete('Famous Mac & Cheese')

print(recipes_box)
del recipes_box[1]
print(recipes_box)

random_recipe = recipes_box.pick()
print('Random recipe is:\n', random_recipe)
picked_recipe = recipes_box.pick('Scrumbled Eggs')
print('Picked recipe is:\n', picked_recipe)

nechita_fridge = Fridge('Nechita\'s Fridge', dictionary_of_products)

print(nechita_fridge)

if 'eggs' in nechita_fridge:
    print('yap')

nechita_fridge.add('salmon', 1)
if 'salmon' in nechita_fridge:
    print ('yap, there is salmon in the fridge')

nechita_fridge.add('eggs', 3)
print ('Now there are ', nechita_fridge['eggs'], ' eggs in the fridge')

print('There are ', nechita_fridge['tomatoes'], ' tomatoes in the fridge')
nechita_fridge.extract('tomatoes', 2)
print('Now there are ', nechita_fridge['tomatoes'], ' tomatoes in the fridge')

print('There is ', nechita_fridge['butter'], 'butter in the fridge')
nechita_fridge.extract('butter', 2)

print('There are ', nechita_fridge['carrots'], 'carrots in the fridge')
nechita_fridge.extract('carrots', 2)
print ('\n')

nechita_fridge.check_recipe(recipes_box.pick())
print ('\n')

my_list=check_the_fridge(nechita_fridge, recipes_box)
if my_list:
    print (my_list)

prepare_shopping_list(nechita_fridge, recipes_box.pick('Simple Pancakes'))
print ("Shopping list archive is: ", shopping_list_archive)