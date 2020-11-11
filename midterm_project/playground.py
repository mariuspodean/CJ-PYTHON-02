
from shopping_list import Recipe
from shopping_list import RecipesBox
from shopping_list import Fridge
from shopping_list import PrintRecipe
import shopping_list


cheesy_potatoes_ingredients = {'potatoes': 500,'butter': 100,'cheese': 300,'milk': 150}
omelette_with_mushrooms_ingredients = { 'eggs': 2,'mushrooms':100,'butter': 10,'onion': 1}
pasta_wtith_tuna_ingredients = { 'pasta': 500, 'tuna' : 100, 'garlic': 2, 'onion' : 2, 'tomata sauce' : 300, 'olive oil' : 10}
prosciutto_and_egg_panini_ingredients = { 'bread': 1, 'egg': 2, 'prosciutto': 200, 'cheese': 100}
barbaque_chicken_sandwiches_ingredients = { 'pepper': 1,'chicken': 100, 'barbaque_sauce': 30, 'bread': 2,'salad': 2} 

cheesy_potatoes_recipe = Recipe( 'Great cheesy potatoes', cheesy_potatoes_ingredients)
omelette_mushrooms_recipe = Recipe ('Yammi omelette', omelette_with_mushrooms_ingredients)
pasta_tuna_recipe = Recipe ('Delicious pasta with tuna', pasta_wtith_tuna_ingredients)
prosciutto_panini_recipe = Recipe ('Delightfull panini', prosciutto_and_egg_panini_ingredients)
chicken_sandwich_recipe = Recipe ('Super sandwich with chicken', barbaque_chicken_sandwiches_ingredients)

print (cheesy_potatoes_recipe['butter'])
print (len(omelette_mushrooms_recipe.ingredients))
print (list (cheesy_potatoes_ingredients.keys()))


prosciutto_panini_recipe = PrintRecipe('Delightfull panini', prosciutto_and_egg_panini_ingredients)
prosciutto_panini_recipe.pretty_printer()


recipes_list = [cheesy_potatoes_recipe, omelette_mushrooms_recipe, pasta_tuna_recipe, prosciutto_panini_recipe,chicken_sandwich_recipe]

box_recipes = RecipesBox (recipes_list)
print (box_recipes[1].name)
print (len (box_recipes.recipes))
print (box_recipes.pick('Great cheesy potatoes').name)

 
fridge = Fridge()
fridge.add_ingredient('potatoes', 500)
fridge.add_ingredient('eggs', 5)
fridge.add_ingredient('pasta', 1000)
fridge.add_ingredient('bread', 3)
fridge.add_ingredient('pepper', 8)
fridge.add_ingredient ('cheese', 500)
fridge.add_ingredient ('chicken', 50)
fridge.update_volume('pepper', 9)
fridge.delete_ingredient('eggs',1)

if 'milk' in fridge:
    print ("Yep, we have it in the fridge")
else:
    print ("No, we don't have it in the fridge")

print(fridge)

ingredients_available, ingredients_to_purchase = fridge.check_recipe (cheesy_potatoes_recipe)
print (f'The ingredients from the recipe that we have in the fridge:' , ingredients_available)

list_recipes = shopping_list.check_the_fridge (fridge, box_recipes)
print (f'We have some of the ingredients for the following recipes :' , list_recipes)


shopping_list.prepare_shopping_list (fridge, chicken_sandwich_recipe)
   

print(shopping_list.shopping_list_archive)