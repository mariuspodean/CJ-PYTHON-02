
##Tennis Tournament Challenge

We are going to design a Tennis Tournament Challenge. Create two classes: 
- Player - which will hold the name, surname, sport and age 
- Tennis Player - which will inherit from Player and also hold points, and a list containing the number of matches played, won, lost in this order. Points and matches will be initiated from 0.

Our Tennis Player class with hold a method 'play' which will:
- Receive another player as an argument
- Randomly decide a winner
- Update the number of points for the two players: 
        - winner will acquire 100 points. 
        - loser will lose 50 points.
- Update the number of matches list: total played, won and lost

####Tournament
Create a function 'tournament' that will simulate our competition, and will take a list of players. 

Each player is expected to play each of the other players once, using the play method (eg. for 6 players, each player will play 5 matches). 

####Ranking
At the end of the Tournament, using the number of points acquired, establish the ranking of our Players with a function called ranking. 

Using operation overloading, ensure that you can sort the players by their number of points using the built in sort function.

The function will return the ranking of the players, starting with the one that has the most points. 

####Decorator
Use a decorator to nicely print the Players' ranking, like in the example below (you can use ascii art )
____________________________________________________________________

**Tennis Tournament Final Ranking**

*1. Player 1, Points: 500*

*2. Player 2, Points: 300*

*3. Player 3, Points: 100*
____________________________________________________________________

