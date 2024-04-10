from random import randint


def disp_Board(arr):
    box = 3

    for row in arr:
        print("+---" * box + "+")

        for col in row:
            print("| " + str(col) + " ", end="")

        print("|")

    print("+---" * box + "+")


def get_Empty(arr):
    empty_boxes = []

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] not in ["X", "O"]:
                empty_boxes.append((i, j))

    return empty_boxes


def check_winner(arr, sign):
    diag1 = diag2 = True

    for i in range(3):
        if arr[i][0] == arr[i][1] == arr[i][2] == sign:
            return sign

        if arr[0][i] == arr[1][i] == arr[2][i] == sign:
            return sign

        if arr[i][i] != sign:
            diag1 = False
            
        if arr[i][2 - i] != sign:
            diag2 = False


    if diag1 or diag2:
        return sign


def human_move(board):
    turn = True
    free_fields = get_Empty(board)

    while turn:
        move = input("Enter Your Move: ")

        if not move.isdigit():
            print("Invalid Input! Enter a number between 1 to 9 corresponding to the Board")
        elif int(move) >= 1 and int(move) <= 9:
            move = int(move) - 1
            row = move // 3
            col = move % 3

            if (row, col) in free_fields:
                board[row][col] = "O"
                turn = False
            else:
                print("Wrong Move! The Box is already occupied")
        else:
            print("Invalid Input! Enter a number between 1 to 9 corresponding to the Board")

    return board


def pc_move(board):
    turn = True
    free_fields = get_Empty(board)

    while turn:
        move = randint(0, 9)
        row = move // 3
        col = move % 3
            
        if (row, col) in free_fields:
            board[row][col] = "X"
            break

    return board



def Tik_Tak_Toe():
    board = [[(3 * j + i) + 1 for i in range(3)] for j in range(3)]
    board[1][1] = "X"
    empty = get_Empty(board)
    HUMAN_Turn = True
        
    
    while len(empty) != 0:
        disp_Board(board)

        if HUMAN_Turn:
            print("\nHuman Turn...")
            board = human_move(board)
            winner = check_winner(board, "O")

        else:
            print("\nComputer Turn...")
            board = pc_move(board)
            winner = check_winner(board, "X")
            
        
        if winner in ("X", "O"):
            break

        HUMAN_Turn = not HUMAN_Turn
        empty = get_Empty(board)


    disp_Board(board)

    if winner == "X":
        print("\n[I Win!!]\n")
    elif winner == "O":
        print("\n[You Win!!]\n")
    else:
        print("\n[Tie ;/ ]\n")


Tik_Tak_Toe()