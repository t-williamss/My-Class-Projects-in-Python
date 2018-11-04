# we will use copy to make a deepcopy of the board
import copy
from typing import Generic, List, TypeVar, Any, Tuple

# stack element type variable
S = TypeVar('S')
# queue element type variable
Q = TypeVar('Q')

# the Stack and Queue classes for DFS and BFS

class Stack:
    """A last in first out (LIFO) stack representation where elements are
    pushed and popped from the top. Think of a stack of plates, where you can't
    remove or add a plate in the middle, only take from, or add to, the top

    Attributes:
        the_stack - the list that holds the elements of our stack
    """

    def __init__(self, initial: List[S] = []) -> None:
        """Constructor for a stack, simply sets the stack up with the given list
        if any is provided otherwise empty

        Args:
            initial - optional list of elements to fill the stack with
        """

        # can't have lists (mutable objects in general) as default values as
        # the default is shared among all instances. need to copy here to
        # avoid issues with aliases
        self.the_stack: List[S] = initial[:]

    def __str__(self) -> str:
        """String representation of the stack"""
        return f"The stack contains: {self.the_stack}"

    def is_empty(self) -> bool:
        """Check if stack has no elements

        Returns:
            True if stack has no elements, False otherwise
        """
        return len(self.the_stack) == 0

    def push(self, elt: S) -> None:
        """Add element (elt) to top of stack

        Args:
            elt - an item to add to the stack
        """
        self.the_stack.append(elt)

    def pop(self) -> S:
        """Remove and return the top item in the stack (corresponds to the last
        item in the list)

        Returns:
            the most recently added element
        """
        return self.the_stack.pop()

class Queue:
    """A first in first out (FIFO) queue representation where elements are pushed
    at the end of the queue and popped from the front. Think of a line at an
    amusement park where new people join (pushed) the line at the back and are
    let in (popped) from the front

    Attributes:
        the_queue - the list that holds the elements of our queue
    """

    def __init__(self, initial: List[Q] = []) -> None:
        """Constructor for a queue, simply sets the queue up with the given list
        if any is provided otherwise empty

        Args:
            initial - optional list of elements to fill the queue with
        """

        # can't have lists (mutable objects in general) as default values as
        # the default is shared among all instances. need to copy here to
        # avoid issues with aliases
        self.the_queue: List[Q] = initial[:]

    def __str__(self) -> str:
        """String representation of the queue"""
        return f"The queue contains: {self.the_queue}"

    def is_empty(self) -> bool:
        """Check if queue has no elements

        Returns:
            True if queue has no elements, False otherwise
        """
        return len(self.the_queue) == 0

    def push(self, elt: Q) -> None:
        """Add element (elt) to end of queue

        Args:
            elt - an item to add to the queue
        """
        self.the_queue.append(elt)

    def pop(self) -> Q:
        """Remove and return the start of the queue (corresponds to the first
        item in the list)

        Returns:
            the oldest added element
        """
        return self.the_queue.pop(0)

# HELPER FUNCTION TO REMOVE ITEMS FROM A LIST
def remove_if_exists(lst: Any, elem: Any) -> None:
    """Takes a list and element and removes that element if it exists in the list

    Args:
        lst - the list you're trying to remove an item from
        elem - item to remove
    """
    if isinstance(lst, list) and elem in lst: lst.remove(elem)

# NOTE: The linter will complain at you due to the code using member variables
# like row, num_nums_placed & size since you haven't added those in the
# constructor. Implement the constructor before worrying about these errors (if
# they're still there after you've implemented the constructor that's probably a
# sign your constructor has a bug in it)
class Board:
    """Represents a state (situation) in a Sudoku puzzle. Some cells may have
    filled in numbers while others have not. Cells that have not been filled in
    hold the potential values that could be assigned to the cell (i.e. have not
    been ruled out from the row, column or subgrid)

    Attributes:
        num_nums_placed - number of numbers placed so far (initially 0)
        size - the size of the board (this will always be 9, but is convenient
            to have an attribute for this for debugging purposes)
        rows - a list of 9 lists, each with 9 elements (imagine a 9x9 sudoku
            board). Each element will itself be a list of the numbers that
            remain possible to assign in that square. Initially, each element
            will contain a list of the numbers 1 through 9 (so a triply nested
            9x9x9 list to start) as all numbers are possible when no assignments
            have been made. When an assignment is made this innermost element
            won't be a list of possibilities anymore but the single number that
            is the assignment.
    """

    def __init__(self):
        """Constructor for a board, sets up a board with each element having all
        numbers as possibilities"""
        self.size: int = 9
        self.num_nums_placed: int = 0

        # triply nested lists, representing a 9x9 sudoku board
        # 9 quadrants, 9 cells in each 3*3 subgrid, 9 possible numbers in each cell
        # Note: using Any in the type hint since the cell can be either a list
        # (when it has not yet been assigned a value) or a value (once it has
        # been assigned)
        # Note II: a lone underscore is a common convention for unused variables
        self.rows: List[List[Any]] = (
        [[list(range(1, 10)) for _ in range(self.size)] for _ in range(self.size)])

    def __str__(self) -> str:
        """String representation of the board"""
        row_str = ''
        for r in self.rows: row_str += f'{r}\n'

        return f'num_nums_placed: {self.num_nums_placed}\nboard (rows): \n{row_str}'

    def print_pretty(self):
        """Prints all numbers assigned to cells, excluding lists of possible
        numbers that can still be assigned to cells."""
        row_str = ''
        for i, r in enumerate(self.rows):
            if not i % 3: row_str += "—————————————————————————\n"

            for j, x in enumerate(r):
                if not j % 3: row_str += "｜"
                row_str += '* ' if isinstance(x, list) else f'{x} '

            row_str += "｜\n"

        row_str += "—————————————————————————\n"
        print(f'num_nums_placed: {self.num_nums_placed}\nboard (rows): \n{row_str}')

    def subgrid_coordinates(self, row: int, col: int) -> List[Tuple[int, int]]:
        """Get all coordinates of cells in a given cell's subgrid (3x3 space)

        Integer divide to get column & row indices of subgrid then take all
        combinations of cell indices with the row/column indices from those
        subgrids (also known as the outer or Cartesian product)

        Args:
            row - index of the cell's row, 0 - 8
            col - index of the cell's col, 0 - 8

        Returns:
            list of (row, col) that represent all cells in the box.
        """
        subgrids = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
        # Note: row // 3 gives the index of the subgrid for the row index, this
        # is one of 0, 1 or 2, col // 3 gives us the same for the column
        return [(r, c) for c in subgrids[col // 3] for r in subgrids[row // 3]]

    def find_most_constrained_cell(self) -> Tuple[int, int]:
        """Finds the coordinates (row and column indices) of the cell that
        contains the fewest possible values to assign (the shortest list). Note:
        in the case of ties return the coordinates of the first minimum size
        cell found

        Returns:
            a tuple of row, column index identifying the most constrained cell
        """
        #min_len = min(len(list))
        min_len = 9
        min_len_x = 0
        min_len_y = 0
        for r in range(9): # we are checking each row 
            for c in range(9):    # we are checking cell by cell
                #self.rows[r][c] # looking at a specific cell 
                #isinstance(x , list)  # in specific cell "is this a list?"
                if isinstance(self.rows[r][c], list):
                    if len(self.rows[r][c]) < min_len: # is length of the specific cell less than min_len
                        min_len = len(self.rows[r][c])
                        min_len_x = r
                        min_len_y = c
        return (min_len_x, min_len_y)

    def failure_test(self) -> bool:
        """Check if we've failed to correctly fill out the puzzle. If we find a
        cell that contains an [], then we have no more possibilities for the cell
        but haven't assigned it a value so fail.

        Returns:
            True if we have failed to fill out the puzzle, False otherwise"""
        for r in range(9): # we are checking each row 
            for c in range(9):    # we are checking cell by cell
                if isinstance(self.rows[r][c], list):
                    if len(self.rows[r][c]) == 0: # is there no length /is it empty 
                        return True
        return False

    def goal_test(self) -> bool:
        """Check if we've completed the puzzle (if we've placed all the numbers).
        Naïvely just checks that we've placed as many numbers as the size of the
        board.

        Returns:
            True if we've placed all numbers, False otherwise
        """
        if self.num_nums_placed == 81:
            return True
        else: 
            return False 
        # for r in range(9): # we are checking each row 
        #     for c in range(9):    # we are checking cell by cell
        #         isinstance(self.rows[r][c], list)
        #         if self.rows[r][c] == []: # is cell equal to an empty list
        #             Return False               
        #         else: 
        #             Return True

    def update(self, row: int, column: int, assignment: int) -> None:
        """Assigns the given value to the cell given by passed in row and column
        coordinates. By assigning we mean set the cell to the value so instead
        the cell being a list of possibities it's just the new assignment value.
        Update all affected cells (row, column & subgrid) to remove the
        possibility of assigning the given value.

        Args:
            row - index of the row to assign
            column - index of the column to assign
            assignment - value to place at given row, column coordinate
        """
        self.rows[row][column] = assignment # assigning the call to a value
        for r, c in self.subgrid_coordinates(row, column):#for the coordinates in self subgrid
            remove_if_exists (self.rows[r][c], assignment) # remove this particular coordinate if it exists in subgrid
        # for cell in self.rows(row, column): 
        #     remove_if_exists (cell.rows, assignment)  # remove this particular coordinate if exists in row 
        for r in range(9): 
            for c in range(9):
                if r == row or c == column:
                    remove_if_exists (self.rows[r][c], assignment) 
        self.num_nums_placed += 1 

def DFS(state: Board) -> Board:
    """Performs a depth first search. Takes a Board and attempts to assign
    values to most constrained cells until a solution is reached or a mistake
    has been made at which point it backtracks.

    Args:
        state - an instance of the Board class to solve, need to find most
        constrained cell and attempt an assignment

    Returns:
        either None in the case of invalid input or a solved board
    """
    S = Stack() 
    S.push(state)
    while not S.is_empty():
        curr = S.pop()
        if curr.goal_test():   #check if it is a goal state if True done if False continue goal_test
            return curr        # check if it is a failure state - failure_test
        elif curr.failure_test():
            r, c = curr.find_most_constrained_cell() #choose a state to look at next == popping something off the stack (call it curr)
            val = curr.rows[r][c] # gets the possbilities now we need to select one and put the others onto the stack 
            curr.update(r , c, val) # find the cell that is most constrained and make an assignment
            for val in state:
                curr_new = copy.deepcopy(curr)
                curr_new.update(r , c, val)
                S.push(curr_new)      
    return None

def BFS(state: Board) -> Board:
    """Performs a breadth first search. Takes a Board and attempts to assign
    values to most constrained cells until a solution is reached or a mistake
    has been made at which point it backtracks.

    Args:
        state - an instance of the Board class to solve, need to find most
        constrained cell and attempt an assignment

    Returns:
        either None in the case of invalid input or a solved board
    """
    Q = Queue() 
    Q.push(state)
    while not Q.is_empty():
        curr = Q.pop()
        if curr.goal_test():   #check if it is a goal state if True done if False continue goal_test
            return curr        # check if it is a failure state - failure_test
        elif curr.failure_test():
            r, c = curr.find_most_constrained_cell() #choose a state to look at next == popping something off the stack (call it curr)
            val = curr.rows[r][c] # gets the possbilities now we need to select one and put the others onto the stack 
            curr.update(r , c, val) # find the cell that is most constrained and make an assignment
            for curr in state:
                curr_new = copy.deepcopy(curr)
                curr_new.update(r , c, val)
                Q.push(curr_new)      
    return None

# first game
b = Board()
first_moves = [
    (0, 1, 7), (0, 7, 1), (1, 2, 9), (1, 3, 7), (1, 5, 4), (1, 6, 2), (2, 2, 8),
    (2, 3, 9), (2, 6, 3), (3, 1, 4), (3, 2, 3), (3, 4, 6), (4, 1, 9), (4, 3, 1),
    (4, 5, 8), (4, 7, 7), (5, 4, 2), (5, 6, 1), (5, 7, 5), (6, 2, 4), (6, 5, 5),
    (6, 6, 7), (7, 2, 7), (7, 3, 4), (7, 5, 1), (7, 6, 9), (8, 1, 3), (8, 7, 8)]

for move in first_moves:
    b.update(*move)

b.print_pretty()

solution = DFS(b)
solution.print_pretty()

# second game
b = Board()

second_moves = [
    (0, 1, 2), (0, 3, 3), (0, 5, 5), (0, 7, 4), (1, 6, 9), (2, 1, 7), (2, 4, 4),
    (2, 7, 8), (3, 0, 1), (3, 2, 7), (3, 5, 9), (3, 8, 2), (4, 1, 9), (4, 4, 3),
    (4, 7, 6), (5, 0, 6), (5, 3, 7), (5, 6, 5), (5, 8, 8), (6, 1, 1), (6, 4, 9),
    (6, 7, 2), (7, 2, 6), (8, 1, 4), (8, 3, 8), (8, 5, 7), (8, 7, 5)]

for move in second_moves:
    b.update(*move)

b.print_pretty()

solution = DFS(b)
solution.print_pretty()

# CODE TO PLAY SUDOKU YOURSELF
# the code below lets you play sudoku yourself, can't let the computers have all
# the fun :) uncomment the lines at the very bottom of the file to play!

def is_valid(board: Board, row_input: int, col_input: int, val_input: int) -> bool:
    """Checks to see if the move you're trying to make is valid

        Returns:
            True if valid, False else"""

    # check for subgrid
    for i, j in board.subgrid_coordinates(row_input, col_input):
        if val_input == board.rows[i][j]:
            return False

    # check for row
    row_attempting = board.rows[row_input]
    for cell in row_attempting:
        if val_input == cell:
            return False

    # column getter
    # loop through rows and add columns
    col_lists = []
    for r in board.rows:
        col_lists.append(r[col_input])

    for val in col_lists:
        if val_input == val:
            return False

    return True

def play_sudoku(b: Board) -> None:
    """Uses your class to play TicTacToe"""
    while not b.goal_test() or b.failure_test():
        b.print_pretty()

        # validate inputs individually
        val_in = int(input(f"What number (1-9) would you like to place?  "))
        if(val_in > 9 or val_in < 1):
            print("\n *********** Invalid value. Try again. *********\n")
            continue

        row_in = int(input(f"Enter row (0-8) to place {val_in} in:  "))
        if(row_in > 8 or row_in < 0):
            print("\n********* Invalid row. Try again from the start. *********\n")
            continue

        col_in = int(input(f"Enter column (0-8) to place {val_in} in:  "))
        if(col_in > 8 or col_in < 0):
            print("\n********* Invalid column. Try again from the start. ********* \n")
            continue

        print(f"Placing {val_in} at ({row_in}, {col_in}).  \n")


        valid = is_valid(b, row_in, col_in, val_in)
        if(valid):
            b.update(row_in, col_in, val_in)
        else:
            print("\n************ Invalid move - already in row/col/subgrid - TRY AGAIN ************\n")
            continue

    if(b.goal_test):
        print("WOO YOU COMPLETED THE GAME!")

    if(b.failure_test):
        print("There's been a problem. This board won't work")

# uncomment the lines below if you'd like to play
# b = Board()
# for move in first_moves: # change first_moves to second_moves to play that game instead
#     b.update(*move)
# play_sudoku(b)
