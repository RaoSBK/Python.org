board = [" " for i in range(9)]

def print_board():
    print()
    for i in range(3):
        print(board[i*3], '|', board[i*3+1], "|", board[i*3*2])
        print()



def check_win(player):
    win_combination=[
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,5], [2,5,8],
        [0,4,8], [2,4,6],
    ]

    for combo in win_combination:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
        return False
    

def play_game():
    current_player= 'X'

    for turn in range(9):
        print(board)
        pos = int(input("Enter position (0-8)"))
        

        