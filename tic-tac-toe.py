theBoard = {'top-l': ' ', 'top-m': ' ', 'top-r': ' ',
            'mid-l': ' ', 'mid-m': ' ', 'mid-r': ' ',
            'low-l': ' ', 'low-m': ' ', 'low-r': ' '}
def print_board(board):
    print(board['top-l'] + '|' + board['top-m'] + '|' + board['top-r'])
    print('-+-+-')
    print(board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-r'])
    print('-+-+-')
    print(board['low-l'] + '|' + board['low-m'] + '|' + board['low-r'])

def play_turn(board, player):
    print_board(board)
    while (True):
        play = input("Player " + player + "'s turn. Enter your play: ")
        if validate_play(board, play):
            board[play] = player
            break
        print("Invalid play.")
        print_board(board)

def validate_play(board, play):
    return play.lower() in board.keys() and board[play] == ' '

def check_result(board):
    if board['top-l'] == board['top-m'] == board['top-r'] or board['mid-l'] == board['mid-m'] == board['mid-r'] or board['low-r'] == board['low-m'] == board['low-l'] or board['top-l'] == board['mid-l'] == board['low-l'] or board['top-m'] == board['mid-m'] == board['low-m'] or board['top-r'] == board['mid-r'] == board['low-r'] or board['top-l'] == board['mid-m'] == board['low-r'] or board['top-r'] == board['mid-m'] == board['low-l']:
        return True
    return False

def start_game():
    board = theBoard
    players = ['O', 'X']
    turn = 0

    for i in range(9):
        play_turn(board, players[turn])
        if i >= 4 and check_result(board):
            print_board(board)
            print("Player " + players[turn] + " has won.")
            break
        if i == 8:
            print("Match drawn")
            break
        turn = (turn + 1) % 2


if __name__ == '__main__':
    start_game()