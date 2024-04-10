import random
import string


remaining_trial = 7
random_numb = str(random.randint(1000, 9999))
print(random_numb)

# rand = random.choices(txt, k=5)
# print(rand)

def game_point_checkpoint(usr, randal):
    bull_cows = [0, 0]
    for i in range(len(randal)):
        if usr[i] == randal[i]:
            bull_cows[0] += 1
        elif usr[i] in randal:
            bull_cows[1] += 1
    return bull_cows

while remaining_trial > 0:
    user_guess = input("Enter a number: ")
    if user_guess == random_numb:
        print("Congrats, you gueessed correctly")
        print("YOU WON")
    if len(user_guess) != len(random_numb):
        print("Sorry, Invalid Numb, Please make sure that the number contains 6 digits only")
        break
    elif len(user_guess) == len(random_numb):
        bull_cows_points = game_point_checkpoint(user_guess, random_numb)
        bulls = bull_cows_points[0]
        cows = bull_cows_points[1]
    
        print('bulls:', bulls)
        print('cows', cows)

        remaining_trial -= 1

        if remaining_trial < 1:
            print("|| Sorry, you have lost the game ||")
