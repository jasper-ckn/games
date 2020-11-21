# Tic Tac Toe

theBoard = {
    '7': ' ', '8': ' ', '9': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '1': ' ', '2': ' ', '3': ' ',
}

player = 1          # To initialise first player
total_moves = 0     # To count the moves
end_check = 0


def check():
    # Checking the moves of player one
    # Check for every horizontal 
    if theBoard['7'] == 'X' and theBoard['8'] == 'X' and theBoard['9'] == 'X':
        print("Player One Won!")
        return 1
    if theBoard['4'] == 'X' and theBoard['5'] == 'X' and theBoard['6'] == 'X':
        print("Player One Won!")
        return 1
    if theBoard['1'] == 'X' and theBoard['2'] == 'X' and theBoard['3'] == 'X':
        print("Player One Won!")
        return 1

    # Checking for every Diagonal (Player One)
    if theBoard['1'] == 'X' and theBoard['5'] == 'X' and theBoard['9'] == 'X':
        print("Player One Won!")
        return 1
    if theBoard['7'] == 'X' and theBoard['5'] == 'X' and theBoard['3'] == 'X':
        print("Player One Won!")
        return 1

    # Checking the moves of every Vertical (Player One)
    if theBoard['7'] == 'X' and theBoard['4'] == 'X' and theBoard['1'] == 'X':
        print('Player One Won!')
        return 1
    if theBoard['8'] == 'X' and theBoard['5'] == 'X' and theBoard['2'] == 'X':
        print("Player One Won!")
        return 1
    if theBoard['9'] == 'X' and theBoard['6'] == 'X' and theBoard['3'] == 'X':
        print("Player One Won!")
        return 1

    # Checking the moves for Player 2
    # Checking for every Horizontal
    if theBoard['7'] == 'o' and theBoard['8'] == 'o' and theBoard['9'] == 'o':
        print("Player Two Won!")
        return 1
    if theBoard['4'] == 'o' and theBoard['5'] == 'o' and theBoard['6'] == 'o':
        print("Player Two Won!")
        return 1
    if theBoard['1'] == 'o' and theBoard['2'] == 'o' and theBoard['3'] == 'o':
        print("Player Two Won!")
        return 1

    # Checking for every Diagnoal (Player Two)
    if theBoard['1'] == 'o' and theBoard['5'] == 'o' and theBoard['9'] == 'o':
        print("Player Two Won!")
        return 1
    if theBoard['7'] == 'o' and theBoard['5'] == 'o' and theBoard['3'] == 'o':
        print("Player Two Won!")
        return 1

    # Checking for every Vertical (Player Two)
    if theBoard['7'] == 'o' and theBoard['4'] == 'o' and theBoard['1'] == 'o':
        print("Player Two Won!")
        return 1
    if theBoard['8'] == 'o' and theBoard['5'] == 'o' and theBoard['2'] == 'o':
        print("Player Two Won!")
        return 1
    if theBoard['9'] == 'o' and theBoard['6'] == 'o' and theBoard['3'] == 'o':
        print("Player Two Won!")
        return 1
    return 0 # 


print('7 | 8 | 9')
print('--+- -+--')
print('4 | 5 | 6')
print('--+- -+--')
print('1 | 2 | 3')
print("************************************************")

while True:
    print(theBoard['7']+'|'+theBoard['8']+'|'+theBoard['9'])
    print('-+-+-')
    print(theBoard['4']+'|'+theBoard['5']+'|'+theBoard['6'])
    print('-+-+-')
    print(theBoard['1']+'|'+theBoard['2']+'|'+theBoard['3'])
    end_check = check() #store the returned value in end_check
    if total_moves == 9 or end_check == 1:
        break 
    while True:     #To take input from players
        if player == 1:     # choose player
            p1_input = input("Player One: ")
            if p1_input.upper() in theBoard and theBoard[p1_input.upper()] == ' ':
                theBoard[p1_input.upper()] = 'X'
                player = 2
                break
            # On wrong input
            else: 
                print("Invalid Input, Please Try Again")
                continue
        else: 
            p2_input = input("Player Two: ")
            if p2_input.upper() in theBoard and theBoard[p2_input.upper()] == ' ':
                theBoard[p2_input.upper()] = 'o'
                player = 1
                break
            else: 
                print("Invalid Input, Please Try Again")
                continue
    total_moves += 1
    print("************************************************")
    print()