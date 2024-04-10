import pyttsx3


print('choose one from Rock, Papper or Scissors ::')
p1 = input("|| Choose onething among:  rock ,  paper or scissors || Player 1 : ")
p2 = input("|| Choose onething among:  rock ,  paper or scissors || Player 2 : ") 


def game_Checker(player1, player2):
    result = ''
    if player1 == player2:
        print("It's a tie, try again")

    if player1 == 'rock' and player2 == 'scissors':
        result = 'Player 1 wins'

    elif player1 == 'scissors' and player2 == 'papper':
        result = 'Player 1 wins'
  

    elif player1 == 'papper' and player2 == 'rock':
        result = "Player 1 wins"
   

    elif player2 == 'rock' and player1 == 'scissors':
        result = 'Player 2 wins'
    
    elif player2 == 'scissors' and player1 == 'papper':
        result = 'Player 2 wins'

    elif player2 == 'papper' and player1 == 'rock':
        result = "Player 2 wins"

    else:
        result = 'invalid selection'

    return result

print(game_Checker(p1, p2))