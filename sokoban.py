from game_settings import *
import copy

# board = [['+', '+', '+', '+', '+', '+', '+', '+'], ['+', ' ', '.', ' ', ' ', ' ', ' ', '+'], ['+', 'i', ' ', '!', ' ', 'o', ' ', '+'], ['+', ' ', ' ', ' ', '!', ' ', 'o', '+'], ['+', ' ', ' ', ' ', ' ', ' ', ' ', '+'], ['+', '+', '+', '+', '+', '+', '+', '+']]

potential_moves = list(CONTROLS)
board_copy = copy.deepcopy(board)

def make_board(board): # prints out the board in desired format
    for i in range(len(board)):
        for j in range(len(board[i])):
            if j == len(board[i]) - 1:
                print(board[i][j])
            else:
                print(board[i][j], end=' ')

def find_loc(board): # finds the location of the player, returns a tuple
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == SPRITE or board[i][j] == SPRITE_T:
                return (i, j)

def find_targets(original_board): # finds where targets are, returns list of tuples with target coordinates
    targets = []
    for i in range(len(original_board)):
        for j in range(len(original_board[i])):
            if original_board[i][j] == TARGET or original_board[i][j] == BOX_S or original_board[i][j] == SPRITE_T:
                coords = i, j
                targets.append(coords)
    return targets

def check_win(board, targets): # returns True if the all the targets are filled with barrels
    for value in targets:
        if not board[value[0]][value[1]] == BOX_S:
            return False
    return True

def check_sprite_t(board): # returns True if the sprite is on a target
    xy = find_loc(board)
    if board[xy[0]][xy[1]] == SPRITE_T:
        return True
    return False

def check_move(move, board): # returns True if player would not move into wall
    xy = find_loc(board) # xy[0] is the row, xy[1] is the column
    if move == 'd':
        if board[xy[0]][xy[1] + 1] == WALL:
            return False
    if move == 'a':
        if board[xy[0]][xy[1] - 1] == WALL:
            return False
    if move == 'w':
        if board[xy[0] - 1][xy[1]] == WALL:
            return False
    if move == 's':
        if board[xy[0] + 1][xy[1]] == WALL:
            return False
    return True
        
def next_to_brick(move, board): # returns True if player would move into brick
    xy = find_loc(board)
    if move == 'd': 
        if board[xy[0]][xy[1] + 1] == BOX_NS or board[xy[0]][xy[1] + 1] == BOX_S:
            return True
    elif move == 'a':
        if board[xy[0]][xy[1] - 1] == BOX_NS or board[xy[0]][xy[1] - 1] == BOX_S:
            return True
    elif move == 'w':
        if board[xy[0] - 1][xy[1]] == BOX_NS or board[xy[0] - 1][xy[1]] == BOX_S:
            return True
    elif move == 's':
        if board[xy[0] + 1][xy[1]] == BOX_NS or board[xy[0] + 1][xy[1]] == BOX_S:
            return True
    return False

def brick_movable(move, board): # returns True if the brick in the direction of the move is movable(empty space or there is a target)
    xy = find_loc(board)
    if move == 'd': 
        if board[xy[0]][xy[1] + 2] not in [TARGET, EMPTY]:
            return False
    elif move == 'a':
        if board[xy[0]][xy[1] - 2] not in [TARGET, EMPTY]:
            return False
    elif move == 'w':
        if board[xy[0] - 2][xy[1]] not in [TARGET, EMPTY]:
            return False
    elif move == 's':
        if board[xy[0] + 2][xy[1]] not in [TARGET, EMPTY]:
            return False
    return True

def satisfied_brick(move, board):
    xy = find_loc(board)
    if next_to_brick(move, board):
        if move == 'd': 
            if board[xy[0]][xy[1] + 1] == BOX_S:
                return True
        elif move == 'a':
            if board[xy[0]][xy[1] - 1] == BOX_S:
                return True
        elif move == 'w':
            if board[xy[0] - 1][xy[1]] == BOX_S:
                return True
        elif move == 's':
            if board[xy[0] + 1][xy[1]] == BOX_S:
                return True
        return False

def empty_move(move, board):
    xy = find_loc(board) # xy[0] is the row, xy[1] is the column
    if check_sprite_t(board):
        if move == 'd':
            if board[xy[0]][xy[1] + 1] == EMPTY:
                board[xy[0]][xy[1]] = TARGET
                board[xy[0]][xy[1] + 1] = SPRITE
                return board
            elif board[xy[0]][xy[1] + 1] == TARGET:
                board[xy[0]][xy[1]] = TARGET
                board[xy[0]][xy[1] + 1] = SPRITE_T
                return board
        if move == 'a':
            if board[xy[0]][xy[1] - 1] == EMPTY:
                board[xy[0]][xy[1]] = TARGET
                board[xy[0]][xy[1] - 1] = SPRITE
                return board
            elif board[xy[0]][xy[1] - 1] == TARGET:
                board[xy[0]][xy[1]] = TARGET
                board[xy[0]][xy[1] - 1] = SPRITE_T
                return board
        if move == 'w':
            if board[xy[0] - 1][xy[1]] == EMPTY:
                board[xy[0]][xy[1]] = TARGET
                board[xy[0] - 1][xy[1]] = SPRITE
                return board
            elif board[xy[0] - 1][xy[1]] == TARGET:
                board[xy[0]][xy[1]] = TARGET
                board[xy[0] - 1][xy[1]] = SPRITE_T
                return board
        if move == 's':
            if board[xy[0] + 1][xy[1]] == EMPTY:
                board[xy[0]][xy[1]] = TARGET
                board[xy[0] + 1][xy[1]] = SPRITE
                return board
            elif board[xy[0] + 1][xy[1]] == TARGET:
                board[xy[0]][xy[1]] = TARGET
                board[xy[0] + 1][xy[1]] = SPRITE_T
                return board
    else:
        if move == 'd':
            if board[xy[0]][xy[1] + 1] == EMPTY:
                board[xy[0]][xy[1]] = EMPTY
                board[xy[0]][xy[1] + 1] = SPRITE
                return board
            elif board[xy[0]][xy[1] + 1] == TARGET:
                board[xy[0]][xy[1]] = EMPTY
                board[xy[0]][xy[1] + 1] = SPRITE_T
                return board
        if move == 'a':
            if board[xy[0]][xy[1] - 1] == EMPTY:
                board[xy[0]][xy[1]] = EMPTY
                board[xy[0]][xy[1] - 1] = SPRITE
                return board
            elif board[xy[0]][xy[1] - 1] == TARGET:
                board[xy[0]][xy[1]] = EMPTY
                board[xy[0]][xy[1] - 1] = SPRITE_T
                return board
        if move == 'w':
            if board[xy[0] - 1][xy[1]] == EMPTY:
                board[xy[0]][xy[1]] = EMPTY
                board[xy[0] - 1][xy[1]] = SPRITE
                return board
            elif board[xy[0] - 1][xy[1]] == TARGET:
                board[xy[0]][xy[1]] = EMPTY
                board[xy[0] - 1][xy[1]] = SPRITE_T
                return board
        if move == 's':
            if board[xy[0] + 1][xy[1]] == EMPTY:
                board[xy[0]][xy[1]] = EMPTY
                board[xy[0] + 1][xy[1]] = SPRITE
                return board
            elif board[xy[0] + 1][xy[1]] == TARGET:
                board[xy[0]][xy[1]] = EMPTY
                board[xy[0] + 1][xy[1]] = SPRITE_T
                return board
            
def moving_block(move, board): # FIX: moving box off of target
    xy = find_loc(board)
    if check_sprite_t(board):
        if satisfied_brick(move, board): # FIX THIS
                if move == 'd':
                    if board[xy[0]][xy[1] + 2] == EMPTY:
                        board[xy[0]][xy[1]] = TARGET
                        board[xy[0]][xy[1] + 1] = SPRITE_T
                        board[xy[0]][xy[1] + 2] = BOX_NS
                        return board
                    elif board[xy[0]][xy[1] + 2] == TARGET:
                        board[xy[0]][xy[1]] = TARGET
                        board[xy[0]][xy[1] + 1] = SPRITE_T
                        board[xy[0]][xy[1] + 2] = BOX_S
                        return board
                if move == 'a':
                    if board[xy[0]][xy[1] - 2] == EMPTY:
                        board[xy[0]][xy[1]] = TARGET
                        board[xy[0]][xy[1] - 1] = SPRITE_T
                        board[xy[0]][xy[1] - 2] = BOX_NS
                        return board
                    elif board[xy[0]][xy[1] - 2] == TARGET:
                        board[xy[0]][xy[1]] = TARGET
                        board[xy[0]][xy[1] - 1] = SPRITE_T
                        board[xy[0]][xy[1] - 2] = BOX_S
                        return board
                if move == 'w':
                    if board[xy[0] - 2][xy[1]] == EMPTY:
                        board[xy[0]][xy[1]] = TARGET
                        board[xy[0] - 1][xy[1]] = SPRITE_T
                        board[xy[0] - 2][xy[1]] = BOX_NS
                        return board
                    elif board[xy[0] - 2][xy[1]] == TARGET:
                        board[xy[0]][xy[1]] = TARGET
                        board[xy[0] - 1][xy[1]] = SPRITE_T
                        board[xy[0] - 2][xy[1]] = BOX_S
                        return board
                if move == 's':
                    if board[xy[0] + 2][xy[1]] == EMPTY:
                        board[xy[0]][xy[1]] = TARGET
                        board[xy[0] + 1][xy[1]] = SPRITE_T
                        board[xy[0] + 2][xy[1]] = BOX_NS
                        return board
                    elif board[xy[0] + 2][xy[1]] == TARGET:
                        board[xy[0]][xy[1]] = TARGET
                        board[xy[0] + 1][xy[1]] = SPRITE_T
                        board[xy[0] + 2][xy[1]] = BOX_S
                        return board
        else:
            if move == 'd':
                if board[xy[0]][xy[1] + 2] == EMPTY:
                    board[xy[0]][xy[1]] = TARGET
                    board[xy[0]][xy[1] + 1] = SPRITE
                    board[xy[0]][xy[1] + 2] = BOX_NS
                    return board
                elif board[xy[0]][xy[1] + 2] == TARGET:
                    board[xy[0]][xy[1]] = TARGET
                    board[xy[0]][xy[1] + 1] = SPRITE
                    board[xy[0]][xy[1] + 2] = BOX_S
                    return board
            if move == 'a':
                if board[xy[0]][xy[1] - 2] == EMPTY:
                    board[xy[0]][xy[1]] = TARGET
                    board[xy[0]][xy[1] - 1] = SPRITE
                    board[xy[0]][xy[1] - 2] = BOX_NS
                    return board
                elif board[xy[0]][xy[1] - 2] == TARGET:
                    board[xy[0]][xy[1]] = TARGET
                    board[xy[0]][xy[1] - 1] = SPRITE
                    board[xy[0]][xy[1] - 2] = BOX_S
                    return board
            if move == 'w':
                if board[xy[0] - 2][xy[1]] == EMPTY:
                    board[xy[0]][xy[1]] = TARGET
                    board[xy[0] - 1][xy[1]] = SPRITE
                    board[xy[0] - 2][xy[1]] = BOX_NS
                    return board
                elif board[xy[0] - 2][xy[1]] == TARGET:
                    board[xy[0]][xy[1]] = TARGET
                    board[xy[0] - 1][xy[1]] = SPRITE
                    board[xy[0] - 2][xy[1]] = BOX_S
                    return board
            if move == 's':
                if board[xy[0] + 2][xy[1]] == EMPTY:
                    board[xy[0]][xy[1]] = TARGET
                    board[xy[0] + 1][xy[1]] = SPRITE
                    board[xy[0] + 2][xy[1]] = BOX_NS
                    return board
                elif board[xy[0] + 2][xy[1]] == TARGET:
                    board[xy[0]][xy[1]] = TARGET
                    board[xy[0] + 1][xy[1]] = SPRITE
                    board[xy[0] + 2][xy[1]] = BOX_S
                    return board
    else:
        if satisfied_brick(move, board): # FIX THIS
                if move == 'd':
                    if board[xy[0]][xy[1] + 2] == EMPTY:
                        board[xy[0]][xy[1]] = EMPTY
                        board[xy[0]][xy[1] + 1] = SPRITE_T
                        board[xy[0]][xy[1] + 2] = BOX_NS
                        return board
                    elif board[xy[0]][xy[1] + 2] == TARGET:
                        board[xy[0]][xy[1]] = EMPTY
                        board[xy[0]][xy[1] + 1] = SPRITE_T
                        board[xy[0]][xy[1] + 2] = BOX_S
                        return board
                if move == 'a':
                    if board[xy[0]][xy[1] - 2] == EMPTY:
                        board[xy[0]][xy[1]] = EMPTY
                        board[xy[0]][xy[1] - 1] = SPRITE_T
                        board[xy[0]][xy[1] - 2] = BOX_NS
                        return board
                    elif board[xy[0]][xy[1] - 2] == TARGET:
                        board[xy[0]][xy[1]] = EMPTY
                        board[xy[0]][xy[1] - 1] = SPRITE_T
                        board[xy[0]][xy[1] - 2] = BOX_S
                        return board
                if move == 'w':
                    if board[xy[0] - 2][xy[1]] == EMPTY:
                        board[xy[0]][xy[1]] = EMPTY
                        board[xy[0] - 1][xy[1]] = SPRITE_T
                        board[xy[0] - 2][xy[1]] = BOX_NS
                        return board
                    elif board[xy[0] - 2][xy[1]] == TARGET:
                        board[xy[0]][xy[1]] = EMPTY
                        board[xy[0] - 1][xy[1]] = SPRITE_T
                        board[xy[0] - 2][xy[1]] = BOX_S
                        return board
                if move == 's':
                    if board[xy[0] + 2][xy[1]] == EMPTY:
                        board[xy[0]][xy[1]] = EMPTY
                        board[xy[0] + 1][xy[1]] = SPRITE_T
                        board[xy[0] + 2][xy[1]] = BOX_NS
                        return board
                    elif board[xy[0] + 2][xy[1]] == TARGET:
                        board[xy[0]][xy[1]] = EMPTY
                        board[xy[0] + 1][xy[1]] = SPRITE_T
                        board[xy[0] + 2][xy[1]] = BOX_S
                        return board
        else:
            if move == 'd':
                if board[xy[0]][xy[1] + 2] == EMPTY:
                    board[xy[0]][xy[1]] = EMPTY
                    board[xy[0]][xy[1] + 1] = SPRITE
                    board[xy[0]][xy[1] + 2] = BOX_NS
                    return board
                elif board[xy[0]][xy[1] + 2] == TARGET:
                    board[xy[0]][xy[1]] = EMPTY
                    board[xy[0]][xy[1] + 1] = SPRITE
                    board[xy[0]][xy[1] + 2] = BOX_S
                    return board
            if move == 'a':
                if board[xy[0]][xy[1] - 2] == EMPTY:
                    board[xy[0]][xy[1]] = EMPTY
                    board[xy[0]][xy[1] - 1] = SPRITE
                    board[xy[0]][xy[1] - 2] = BOX_NS
                    return board
                elif board[xy[0]][xy[1] - 2] == TARGET:
                    board[xy[0]][xy[1]] = EMPTY
                    board[xy[0]][xy[1] - 1] = SPRITE
                    board[xy[0]][xy[1] - 2] = BOX_S
                    return board
            if move == 'w':
                if board[xy[0] - 2][xy[1]] == EMPTY:
                    board[xy[0]][xy[1]] = EMPTY
                    board[xy[0] - 1][xy[1]] = SPRITE
                    board[xy[0] - 2][xy[1]] = BOX_NS
                    return board
                elif board[xy[0] - 2][xy[1]] == TARGET:
                    board[xy[0]][xy[1]] = EMPTY
                    board[xy[0] - 1][xy[1]] = SPRITE
                    board[xy[0] - 2][xy[1]] = BOX_S
                    return board
            if move == 's':
                if board[xy[0] + 2][xy[1]] == EMPTY:
                    board[xy[0]][xy[1]] = EMPTY
                    board[xy[0] + 1][xy[1]] = SPRITE
                    board[xy[0] + 2][xy[1]] = BOX_NS
                    return board
                elif board[xy[0] + 2][xy[1]] == TARGET:
                    board[xy[0]][xy[1]] = EMPTY
                    board[xy[0] + 1][xy[1]] = SPRITE
                    board[xy[0] + 2][xy[1]] = BOX_S
                    return board
    

def play_game(board):
    global board_copy
    original_copy = copy.copy(board_copy)
    targets = find_targets(original_copy)
    continue_game = True
    while continue_game:
        if check_win(board, targets):
            make_board(board)
            print('You Win!')
            break
        make_board(board)
        print()
        move = input()
        move = move.lower()
        while move not in potential_moves:
            move = input('enter a valid move:\n')
        if move == 'q': # ends game
            print('Goodbye')
            continue_game = False
        elif move == ' ': # FIX returning to original board
            board = copy.deepcopy(original_copy)
        else:
            if check_move(move, board):
                if not next_to_brick(move, board):
                    board = empty_move(move, board)
                elif next_to_brick(move, board) and brick_movable(move, board):
                    board = moving_block(move, board)
play_game(board)
