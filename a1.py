"""Assignment 1

Fill in the following function skeletons - descriptions are provided in the PDF,
and briefly in the docstring (the triple quote thing at the top of each function)

Some assert statements have been provided - write more of them to test your code!
"""

from typing import List, TypeVar

#####################################################################################################
def absolute(n: int) -> int:

    
    """Gives the absolute value of the passed in number. Cannot use the built
    in function `abs`.

    Args:
        n - the number to take the absolute value of

    Returns:
        the absolute value of the passed in number
    """
    absolute_val = 0
    if(n < 0):
        absolute_val = n*(-1)
    else:
        absolute_val = n

    return absolute_val
assert absolute(-1) == 1, "absolute of -1 failed"
assert absolute(9) == 9, "absolute of 9"

##################################################################################################################################
def factorial(n: int) -> int:
    """Takes a number n, and computed the factorial n!

    Args:
        n - the number to do factorial of

    Returns:
        factorial of the passed in number
    """
    if(n == 0 or n == 1):
        return 1
    else: 
        return n*factorial(n-1)

assert factorial(4) == 24, "factorial of 4 failed"
assert factorial(9) == 362880, "factorial of 9 is successful"

#########################
T = TypeVar('T')
def every_other(lst: List[T]) -> List[T]:
    """Takes a list and returns a list of every other element in the list,
    starting with the first.

    Args:
        lst - a list of any (constrained by type T to be the same type as the
            returned list)

    Returns:
        a list of every of other item in the original list starting with the first
    """
 
    # #x = len(lst)
    # every_other = [x]
    # if len(lst)%2 == 0
    #     del #that item 
    # else: every_other = every_other
    #     print(every_other)

    # return every_other 

    new_lst = []
    for index in range(len(lst)):
        if(index%2 == 0):
            new_lst.append(lst[index])
    return new_lst   
    
assert every_other([1,2,3,4,5]) == [1,3,5], "every_other of [1,2,3,4,5] failed"

#########################
def sum_list(lst: List[int]) -> int:
    """Takes a list of numbers, and returns the sum of the numbers in that list.
    Cannot use the built in function `sum`.

    Args:
        lst - a list of numbers

    Returns:
        the sum of the passed in list
    """
    sum = 0
    for x in lst: 
        sum += x
    return sum
        
assert sum_list([1,2,3]) == 6, "sum_list of [1,2,3] failed"

######################################################################################
def mean(lst: List[int]) -> float:
    """Takes a list of numbers, and returns the mean of the numbers.

    Args:
        lst - a list of numbers

    Returns:
        the mean of the passed in list
    """

    return sum(lst)/(len(lst))

assert mean([1,2,3,4,5]) == 3, "mean of [1,2,3,4,5] failed"

############################################################################
def median(lst: List[int]) -> float:
    """Takes an ordered list of numbers, and returns the median of the numbers.
    If the list has an even number of values, it computes the mean of the two
    center values.

    Args:
        lst - an ordered list of numbers

    Returns:
        the median of the passed in list
    """
    if((len(lst))%2 == 0):
        left = len(lst)//2 - 1
        right = len(lst)//2
        return(lst[left]+lst[right])/2
    else:
        mid = len(lst)//2
        return lst[mid]
    # if list has even number of elements (check this by doing len(lst)%2==0)
    # find two middle elements and take mean of those
    # len(lst)/2 - 1for the leftmost middle element
    # len(lst)/2 for the rightmssost elemenet

    # left = 
    # right

    # return (lst[left]+lst[right])/2

    # put  this inside of an else 
    # if list has odd number of elements
    # return element at middle index
    # mid = len(lst) // 2
    # floor division: // (so 3//2 = 1)
    # return lst[mid]

    # if:
        # asdadsasd
        # return
    #else:
        # asdasd
        # return

        #split into even case or odd case 
       # return 

assert median([1,2,3,4,5]) == 3, "median of [1,2,3,4,5] failed"
assert median([1,2,3,4]) == 2.5, "median of [1,2,3,4,] failed"
assert median([1]) == 1, "median of [1] failed"
#############################################################################3#########################
def duck_duck_goose(lst: List[str]) -> List[str]:
    """Given an list of names (strings), play 'duck duck goose' with it,
    knocking out every third name (wrapping around) until only two names are
    left. In other words, when you hit the end of the list, wrap around and keep
    counting from where you were.

    For example, if given this list ['Nathan', 'Sasha', 'Sara', 'Jennie'], you'd
    first knock out Sara. Then first 'duck' on Jennie, wrap around to 'duck' on
    Nathan and 'goose' on Sasha - knocking him out and leaving only Nathan and
    Jennie.

    You may assume the list has 3+ names to start

    Args:
        lst - a list of names (strings)

    Returns:
        the resulting list after playing duck duck goose
    """
    index = 0
    state = "duck-1"

    while(len(lst)) > 2:
        if(state == "duck-1"):
            state = "duck-2"
            index += 1 
        elif(state == "duck-2"):
            state = "goose"
            index += 1 
        else: 
            lst.pop(index)
            state = "duck-1"

        if(index >= len(lst)):
            index = index - len(lst)
    return lst 
            
        

names = ["sasha", "nathan", "jennie", "shane", "will", "sara"]
assert duck_duck_goose(names) == ["sasha", "will"]

print(duck_duck_goose(names))
