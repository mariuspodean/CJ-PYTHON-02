Dear Student!

Your challenge is to create a game, named "Roulette".

Create a class "Player", where you will create at least 3 players, with a name, age and an amount credit they want to play with.
When creating the players, you must verify if their age is legal to play or not (age>18). After creating the players, printing their infos will look like:
   1. John Doe, age 20, credit: 1000 $.
   2. George Dragan, age 26, credit: 2000$
   ...

Create an other class "Betting" that will set the bettings. 
On the roulette table they can bet any amount of credit they want, on different betting-options:
   1. on any number between 1-36
   2. by color (red/black)
   3. even / odd number
   4. low / high bet

A random number or color will be given to verify who wins. Using operator overloading, verify who has the highest number, the player or the table.
By these different cases of betting, the player will get different winpoints: case 1: 100% bonus of the amount he was betting. Case 2 and 3: 50% bonus of the amount he was betting. Case 4: 30%.  If the table wins, the player will loose the amount he was betting.
If a player's credit gets to 0, the player must leave the table (by removing the player).
If a player wins, using a decorator method, print out the following text, that includes the winners name, and the amount he won:

  ----------------------------------
  |********************************|
  |** Congratulations George D. ***|
  |******** You won 200 $ *********|
  |********************************|
  |******** Good luck! ************|
  |********************************|
  ----------------------------------

As an optional task, when a player wins, add the amount to his credit and ask him if he wants to continue or to exit.
If he quits, print out his fullname, and the total credit.
