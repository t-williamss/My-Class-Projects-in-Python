from typing import List

def match(pattern: List[str], source: List[str]) -> List[str]:
    """Attempts to match the pattern to the source. 

    % matches a sequence of zero or more words and _ matches any single word

    Args:
        pattern - a pattern using to % and/or _ to extract words from the source
        source - a phrase represented as a list of words (strings)

    Returns:
        None if the pattern and source do not "match."
        A list if the pattern and source "match." If the pattern contains _ or %'s, 
            the list will contain the substitutions for them from source.
    """
    sind = 0                # current index we are looking at in the source list
    pind = 0                # current index we are looking at in the pattern list
    result: List[str] = []  # to store the substitutions that we will return if matched
    acc = ''

    # keep checking as long as we haven't hit the end of both pattern and source
    while sind != len(source) or pind != len(pattern):    
        # Your job is to fill out the body fo this loop
        # 1) if we reached the end of the pattern but not source 
        if pind == len(pattern):
            return None
        # 2) if the current thing in the pattern is a %
        elif pattern[pind] == '%':
            pind += 1 # moving from % to next word 
            while sind != len(source):
                if pind != len(pattern) and pattern[pind] == source[sind]:
                    break 
                else: 
                    if acc == "": 
                        acc += source[sind] # if it is the first character do not add a space 
                    else: 
                        acc += " "
                        acc += source[sind]
                sind += 1
            result.append(acc)
            acc = ''
        # 3) if we reached the end of the source but not the pattern
        elif sind == len(source):
            return None             
        # 4) if the current thing in the pattern is an _
        elif pattern[pind] == '_':
            result.append(source[sind])
            sind += 1
            pind += 1
            #appending is for lists and adding is for strings
        # 5) if the current thing in the pattern is the same as the current thing 
        #    in the source
        elif pattern[pind] == source[sind]:
            sind += 1
            pind += 1
        # 6) else : this will happen if none of the other conditions are met
        #    it indicates the current thing it pattern doesn't match the current
        #    thing in source
        else: 
            return None
    return result

assert match(['x', 'y', 'z'], ['x', 'y', 'z']) == [], "test 1 failed"
assert match(['x', 'z', 'z'], ['x', 'y', 'z']) == None, "test 2 failed"
assert match(['x', 'y'], ['x', 'y', 'z']) == None, "test 3 failed"
assert match(['x', 'y', 'z', 'z'], ['x', 'y', 'z']) == None, "test 4 failed"
assert match(['x', '_', 'z'], ['x', 'y', 'z']) == ['y'], "test 5 failed"
assert match(['x', '_', '_'], ['x', 'y', 'z']) == ['y', 'z'], "test 6 failed"
assert match(['%'], ['x', 'y', 'z']) == ['x y z'], "test 7 failed"
assert match(['x', '%', 'z'], ['x', 'y', 'z']) == ['y'], "test 8 failed"
assert match(['%', 'z'], ['x', 'y', 'z']) == ['x y'], "test 9 failed"
assert match(['x', '%', 'y'], ['x', 'y', 'z']) == None, "test 10 failed"
assert match(['x', '%', 'y', 'z'], ['x', 'y', 'z']) == [''], "test 11 failed"
assert match(['x', 'y', 'z', '%'], ['x', 'y', 'z']) == [''], "test 12 failed"
assert match(['_', '%'], ['x', 'y', 'z']) == ['x', 'y z'], "test 13 failed"
assert match(['_', '_', '_', '%'], ['x', 'y', 'z']) == ['x', 'y', 'z', ''], "test 14 failed"
# this last case is a strange one, but it exposes an issue
# with the way we've written our match function
assert match(['x', '%', 'z'], ['x', 'y', 'z', 'z', 'z']) == None, "test 15 failed"
