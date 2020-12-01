## ***Operator Overloading Challenge***



#### Create a <u>Budget App</u> to help you manage your income and your expenses. 



You will have the following classes:

- *monthly_budget* (Name, Salary, Gifts, Interest_rate) 
  - use operator overloading to add two monthly budgets  - each attribute from one object will be added to its homologue from the other object 

- *monthly_expenses* (Name, Necessities [50% * salary], Quality[30% * (salary and gifts)], Economies[20% * (salary and interest_rate)])
  - when the user will use more than the allowed percentage from each expenses category, he will receive a warning message 
- *yearly_budget* =[(monthly_budget, monthly_expenses)]
  - starting from the yearly_budget one has to be able to sort the month from the "richest" month to the "poorest" (the richest month is the one where salary+gifts+interest_rate is the highest and the expenses are the lowest in a series of 12  months)

 In order to have a nice display, use a decorator for each class. The design of the decorator is at your choice.

#### ***Bonus:***

Make the sorting of the yearly budget include as a criteria the expenses too in order to find the most profitable month - maximum budget and minimum expenses.





