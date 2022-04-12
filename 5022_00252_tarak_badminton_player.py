''' Tarak is playing badminton today. The service rules of this singles game of badminton are as follows:
The player who starts the game serves from the right side of their court.

Whenever a player wins a point, they serve next.

If the server has won an even number of points during a game, then they will serve from the right side of the service court for the subsequent point.

Tarak will be the player who begins the game.
Given the number of points P obtained by Tarak at the end of the game, please determine how many times Tarak served from the right side of the court.
Please see the sample cases below for explained examples.
Input Format
The first line of input contains a single integer T, denoting the number of test cases. The description of T test cases follows.

Each test case consists of a single line containing one integer P, the points obtained by Tarak.

Output Format
For each test case, output in a single line the number of times Tarak served from the right side of the court.
Sample Input 
4
2
9
53
746
Sample Output
2
5
27
374'''



no_of_test_cases=int(input("No of test Cases "))
for test_cases in range(no_of_test_cases):
    tarak_points=0
    game_points=int(input("Game points "))
    for game_point in range(game_points+1):
        if(game_point%2==0):
            tarak_points=tarak_points+1
    print("Tarak score : ",tarak_points)
