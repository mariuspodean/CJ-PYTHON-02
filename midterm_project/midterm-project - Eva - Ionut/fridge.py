

class Fridge(object):

    def __init__(self):
        self.products_fridge = {}

    def __len__(self):
        return len(self.products_fridge)

    def __getitem__(self, product):
        return self.products_fridge[product]

    def __delitem__(self, product):
        del self.products_fridge[product]

    def __setitem__(self, product, quantity):
        self.products_fridge[product] = quantity
        return f'Quantity of {product} now set at {quantity}'

    def __iter__(self):
        return iter(self.products_fridge)

    def __str__(self):
        stars = '*'*20
        print(stars, '\n', 'Items in Fridge:','\n' )
        for index, (product, quantity) in enumerate(self.products_fridge.items(), start = 1):
            print( f'{index}. {product.title()}: {quantity}')
        return stars

    def add_item(self, product, quantity):
        self.products_fridge[product] = quantity

    def delete_item(self, product):
        del self.products_fridge[product]
        return f'{product} will be removed from the Fridge'

    def remove_quantity_item(self, product, quantity):
        if product in self.products_fridge.keys():
            if self.products_fridge[product] > quantity:
                self.products_fridge[product] -= quantity
                return f'Removing {quantity} of {product}. You now have {self.products_fridge[product]} of {product} left in the Fridge'
            elif self.products_fridge[product] == quantity:
                del self.products_fridge[product]
                return f'Removing {quantity} of {product}. No {product} left. Please buy more!'
            else:
                return f'Insufficient {product} in Fridge. Please adapt quantity to remove'
        else:
            return f'No {product} in the Fridge. Please buy {product}!'

    def add_quantity_item(self, product, quantity):
        if product in self.products_fridge.keys():
            self.products_fridge[product] += quantity
            return f'{product} quantity has been updated with {quantity} in the Fridge. You now have {self.products_fridge[product]}'
        else:
            self.products_fridge[product] = quantity
            return f'You did not have {product} in the Fridge. Quantity now updated to {quantity}'

    def check_recipe(self, recipe):
        items_to_buy = []
        items_in_fridge = []
        for ingredient in recipe.ingredients.keys():
            if ingredient.title() in self.products_fridge.keys():
                items_in_fridge.append(ingredient.title())
            else:
                items_to_buy.append(ingredient.title())
        if items_to_buy and items_in_fridge:
            return f'For the recipe {recipe.name} you already have {items_in_fridge}. You need to buy {items_to_buy}'
        elif not items_to_buy and items_in_fridge:
            return f'You have all the ingredients for the {recipe.name} recipe: {items_in_fridge}'
        else:
            return f'You have none of the ingredients for the {recipe.name} recipe. Go shopping and get {items_to_buy}'


muffin_man_fridge = Fridge()

muffin_man_fridge.add_item('Eggs', 30)
muffin_man_fridge.add_item('Tomatoes', 50)
muffin_man_fridge.add_item('Juice', 4)

print(muffin_man_fridge)

muffin_man_fridge.delete_item('Eggs')
print(muffin_man_fridge)
print(muffin_man_fridge.remove_quantity_item('Juice', 10))
print(muffin_man_fridge.remove_quantity_item('Apples', 13))
print(muffin_man_fridge.remove_quantity_item('Tomatoes', 10))
print(muffin_man_fridge.remove_quantity_item('Tomatoes',40))
print(muffin_man_fridge)

muffin_man_fridge.add_item('Cheese', 30)
muffin_man_fridge.add_item('Halloumi', 50)
muffin_man_fridge.add_item('Veggie Burger', 4)
muffin_man_fridge.add_item('Ham', 10)
muffin_man_fridge.add_item('Bread', 20)

if 'Juice' in muffin_man_fridge:
    print('YES!')

print(muffin_man_fridge)
print(len(muffin_man_fridge))

print(muffin_man_fridge.__getitem__('Juice'))
print(muffin_man_fridge.__setitem__('Juice', 20))
del muffin_man_fridge['Juice']

