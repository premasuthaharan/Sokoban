from game_settings import *
import copy

current_board = copy.deepcopy(board)

row_index = 0
column_index = 0
target_row = 0
target_column = 0

def print_board(cboard):
    for row in cboard:
        for index, element in enumerate(row):
            if index != (len(row) - 1):
                print(element, end=' ')
            else:
                print(element)
    print()

def get_pos(cboard):
    global row_index
    global column_index
    global target_column
    global target_row
    for index1, row in enumerate(cboard):
        for index2, square in enumerate(row):
            if square == SPRITE or square == SPRITE_T:
                row_index = index1
                target_row = index1
                column_index = index2
                target_column = index2
                #print(row_index, target_row, column_index, target_column)
                break

def up():
    global target_row
    target_row -= 1

def down():
    global target_row
    target_row += 1

def left():
    global target_column
    target_column -= 1

def right():
    global target_column
    target_column += 1

def reset():
    global current_board
    current_board = copy.deepcopy(board)
    push = False
    win = False
    removed = EMPTY
    under = EMPTY
    #print('reseting board') #debug

def win_check():
    counter = 0
    win = True
    global current_board

    for row in current_board:
        for square in row:
            if square == TARGET:
                win = False
                #print('target found') #debug
                break

    return win

moves = {'w':up,'s':down,'a':left,'d':right}

push = False
win = False
under = EMPTY
#print('newest') #debug

def valid_check(target_move):
    #print('target_move is', target_move) #debug
    #print('current position is', current_board[row_index][column_index], row_index, column_index) #debug
    target = current_board[target_row][target_column]
    #print('target is', target) #debug
    global push
    global under
    if target == SPRITE or target == SPRITE_T:
        push = False
        return True
    if target == EMPTY:
        push = False
        under = EMPTY
        #print('empty') #debug
        return True
    elif target == WALL:
        #print('wall') #debug
        return False
    elif target == TARGET:
        #print('target') #debug
        under = TARGET
        push = False
        return True
    elif target == BOX_NS or target == BOX_S:
        if target_move == 'w':
            target2 = current_board[target_row-1][target_column]
        elif target_move == 's':
            target2 = current_board[target_row+1][target_column]
        elif target_move == 'a':
            target2 = current_board[target_row][target_column - 1]
        elif target_move == 'd':
            target2 = current_board[target_row][target_column + 1]
        if target2 == WALL or target2 == BOX_NS or target2 == BOX_S:
            #print('target2 is full') #debug
            return False
        else:
            push = True
            if target == BOX_S:
                under = TARGET
                removed2 = TARGET
                #print('special') #debug
            else:
                under = EMPTY
                removed2 = EMPTY
                #print('not special') #debug
            return True

removed = EMPTY
removed2 = EMPTY
print_board(current_board)
get_pos(current_board)
while True:
    move = input()
    #print('removed is', removed)
    if move == 'q':
        print('Goodbye')
        break

    if move == ' ':
        reset()
        removed = EMPTY
        print_board(current_board)
        get_pos(current_board)
        continue
        
    if move in moves.keys():
        moves[move]()
        if valid_check(move):
            #print('executing', move) #debug
            if current_board[row_index][column_index] == SPRITE:
                current_board[row_index][column_index] = EMPTY
            elif current_board[row_index][column_index] == SPRITE_T:
                current_board[row_index][column_index] = TARGET
            #print('replacing old with', removed) #debug
            #removed = current_board[target_row][target_column]
            #print('changing removed to', removed) #debug
            if under == EMPTY:
                current_board[target_row][target_column] = SPRITE
            elif under == TARGET:
                current_board[target_row][target_column] = SPRITE_T
            #else:
                #print(under) #debug
            if push:
                if move == 'w':
                    target_row -= 1
                elif move == 's':
                    target_row += 1
                elif move == 'a':
                    target_column -= 1
                elif move == 'd':
                    target_column += 1
                #print_board(current_board) #debug
                if current_board[target_row][target_column] == TARGET:
                    removed2 == TARGET
                    current_board[target_row][target_column] = BOX_S
                    #print_board(current_board) #debug
                    #print('changed removed to TARGET') #debug
                    removed = TARGET
                elif current_board[target_row][target_column] == EMPTY:
                    removed2 == EMPTY
                    current_board[target_row][target_column] = BOX_NS
                    #print('changed removed to EMPTY') #debug
                    removed = EMPTY
        #else:
            #print('enter a valid move:')
    else:
        print('enter a valid move:')
        continue

    if win_check():
        for row in current_board:
            for index, element in enumerate(row):
                if index != (len(row) - 1):
                    print(element, end=' ')
                else:
                    print(element)
        print('You Win!')
        break

    print_board(current_board)
    get_pos(current_board)
