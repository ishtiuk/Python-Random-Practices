from math import gamma
from operator import le
from random import randint

trials = 5

def point_counter_unit(usr, game_rand):
    bull_cows = [0, 0]              # here, we used a sperate or dedicated Point counter function for the Game 😎😎, 
    for i in range(len(usr)):
        if usr[i] == game_rand[i]:
            bull_cows[0] += 1            # and we Defined a List or Array for counting bulls and cows number Instead of Define them sperately, Like
                                         
        elif usr[i] in game_rand:       # cows = 0
            bull_cows[1] += 1           # bulls = 0   

    return bull_cows                                   

def game_main():
    global trials                               # we are using Recursion or Recursive Function instead of While LOOp 😎😎, look at Line 38, 39, 40

    gm_ran_num = str(randint(100, 200))
    print(gm_ran_num)

    usr = int(input('Guess a Number Between 100 to 200: '))
    usr_str = str(usr)

    if gm_ran_num == usr_str:
        print('Congrats, you have gueessed Correctly')
        trials -= 1

    if (len(gm_ran_num) != len(usr_str)) or (usr < 100 or usr > 200):
        print('Make sure that number is between 100 to 200')

    elif len(gm_ran_num) == len(usr_str):
        points = point_counter_unit(usr_str, gm_ran_num)

        print('bulls: ', points[0])
        print('cows: ', points[1])
        trials -= 1

    if trials > 0:                      # Recursive Function 😎😎
        game_main()

    
game_main()
