# NOTE: Until you fill in the TTTBoard class mypy is going
# to give you multiple errors talking about unimplemented
# class attributes, don't worry about this as you're working

class TTTBoard:
    """A tic tac toe board

    Attributes:
        board - a list of '*'s, 'X's & 'O's. 'X's represent moves by player 'X',
        'O's represent moves by player 'O' and '*'s are spots no one has yet
        played on
    """
    def __init__(self):
        self.board = ["*", "*", "*","*","*","*","*","*","*"]

    def __str__(self):
        b = self.board[0] + self.board[1] + self.board[2]+ "\n"
        b += self.board[3] + self.board[4] + self.board[5]+ "\n"
        b += self.board[6] + self.board[7] + self.board[8]+ "\n"
        return b

    def make_move(self, player, pos):
        if pos in range(9) and self.board[pos] == "*":
            self.board[pos] = player 
            return True
        else: 
            return False    

    def has_won(self, player): 
        if player == self.board[0] == self.board[1] == self.board[2]:
            return True
        if player == self.board[3] == self.board[4] == self.board[5]:
            return True
        if player == self.board[6] == self.board[7] == self.board[8]:
            return True
        if player == self.board[0] == self.board[3] == self.board[6]:
            return True
        if player == self.board[1] == self.board[4] == self.board[7]:
            return True
        if player == self.board[2] == self.board[5] == self.board[8]:
            return True
        if player == self.board[0] == self.board[4] == self.board[8]:
            return True
        if player == self.board[2] == self.board[4] == self.board[6]:
            return True
        else:
            return False

    def game_over(self): 
        if self.has_won("X") or self.has_won("O"): 
            return True 
        else: 
            for x in self.board:
                if x == "*":
                    return False
        return True

    def clear(self): 
        self.board = ["*", "*", "*","*","*","*","*","*","*"]

# Here is my assert for proc: make_move
my_board = TTTBoard()
#print(my_board)
assert my_board.make_move("X", 3) == True 
assert my_board.make_move("O", 9) == False
assert my_board.make_move("O", 3) == False
#print(my_board)

# Here are my asserts for proc: has_won
my_board.make_move("X", 3)
my_board.make_move("X", 4) 
my_board.make_move("X", 5)
assert my_board.has_won("X") == True
#print(my_board)

my_board.make_move("O", 2)
my_board.make_move("O", 4)
my_board.make_move("O", 6)
assert my_board.has_won("O") == False
#print(my_board)

my_board.make_move("O", 2)
my_board.make_move("X", 3)
my_board.make_move("O", 8)
assert my_board.has_won("O") == False
#print(my_board)

# Here is my assert for proc: game_over
my_board.make_move("O", 2)
my_board.make_move("O", 4)
my_board.make_move("O", 6)   
assert my_board.game_over() == True # this is when you have won so game over

# my_board.make_move("X", 2)
# my_board.make_move("X", 5)
# my_board.make_move("X", 0)
# assert my_board.game_over() == True # this is when no one has won so no game over

my_board.make_move("X", 5)
my_board.make_move("O", 6)
my_board.make_move("X", 4)
my_board.make_move("O", 7)
my_board.make_move("O", 8)
my_board.make_move("O", 0)
my_board.make_move("X", 3)
my_board.make_move("X", 2)
my_board.make_move("X", 1)
assert my_board.game_over() == True # this is when the game board is full so game over

# my_board.make_move("X", 5)
# my_board.make_move("O", 6)
# my_board.make_move("X", 4)
# assert my_board.game_over == True # this is when no one has won and there are still empty 
#                                     # spots on the game board so no game over

#Here is my assert for proc: clear(self):


def play_tic_tac_toe() -> None:
    """Uses your class to play TicTacToe"""
    brd = TTTBoard()
    players = ["X", "O"]
    turn = 0

    while not brd.game_over():
        print(brd)
        move: str = input(f"Player {players[turn]} what is your move? ")
        if not move.isdigit():
            raise ValueError(f"Given invalid position {move}, "
                "position must be integer between 0 and 8 inclusive")

        brd.make_move(players[turn], int(move))
        turn = not turn

    print(f"\nGame over!\n\n{brd}")
    if brd.has_won(players[0]):
        print(f"{players[0]} wins!")
    elif brd.has_won(players[1]):
        print(f"{players[1]} wins!")
    else:
        print(f"Board full, cat's game!")


# # here are some tests. These are not at all exhaustive tests. You will
# # DEFINITELY need to write some more tests to make sure that your TTTBoard class
# # is behaving properly.
brd = TTTBoard()
brd.make_move("X", 8)
brd.make_move("O", 7)

assert brd.game_over() == False

brd.make_move("X", 5)
brd.make_move("O", 6)
brd.make_move("X", 2)

assert brd.has_won("X") == True
assert brd.has_won("O") == False
assert brd.game_over() == True

brd.clear()

assert brd.game_over() == False

brd.make_move("O", 3)
brd.make_move("O", 4)
brd.make_move("O", 5)

assert brd.has_won("X") == False
assert brd.has_won("O") == True
assert brd.game_over() == True

print('All tests passed!')

# # uncomment to play!
play_tic_tac_toe()