# **Challenge**
## **Fruit store**
This fruit store needs a way to weigh the fruits that the customers are buying and charge them accordingly!
#### **Fruit Class**
We will have a `Fruit` Class with the following attributes: `type` (_string_), `average_weight` (_int_ **_grams_**) and `price_per_kg` (_float_ **_euro / preffered currency_**). The average_weight and the price_per_kg do not need to be accuarate. Example syntax:
``` python
    apple_product = Fruit('Apple', 300, 1.2)
    banana_product = Fruit('Banana', 200, 1.75)
```
### **ShoppingBag Class**
Once the customers have added their desired fruits to their shopping carts, they will come up to the counter and place their fruits in a shopping bag, one by one. The `ShoppingBag` _class_ will have a way to store **the total weight and the total price** of the fruits added to it. The customer can **_add_** fruits to the shopping bag with the `+=` assignment and **_remove_** fruits with the `-=` assignment.
``` python
    shopping_bag = ShoppingBag()
    shopping_bag += apple_product
    shopping_bag += banana_product
```
Also, if the customer wants to buy more than one of the same fruit, make it so that he can multiply the fruit by a number when adding to the shopping bag using the `*` method
``` python
    shopping_bag += apple_product * 8
```
##### total() method
The `ShoppingBag` class will have a `total()` method that is going to print the current shopping bag's **total weight** and **total price** in a nice string format.
``` python
    shopping_bag.total()
    >'This shopping bag weighs 2.5 kg, and the total cost of the fruit it holds is 6.25 euro'
```
### **Optional task**
##### Adding fruits together
Make it so that the customer can **add** multiple fruits together on the same line to the shopping bag using the `+` method
``` python
    shopping_bag += apple_product + banana_product
```
