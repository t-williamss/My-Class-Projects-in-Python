from typing import List

def match(pattern: List[str], source: List[str]) -> List[str]:
    """Attempts to match the pattern to the source.

    % matches a sequence of zero or more words and _ matches any single word

    Args:
        pattern - a pattern using to % and/or _ to extract words from the source
        source - a phrase represented as a list of words (strings)

    Returns:
        None if the pattern and source do not "match" ELSE
        A list of matched words (words in the source corresponding to _'s or %'s,
            in the pattern, if any)
    """
    sind = 0                # current index we are looking at in the source list
    pind = 0                # current index we are looking at in the pattern list
    result: List[str] = []  # to store the substitutions that we will return if matched

    # keep checking as long as we haven't hit the end of both pattern and source
    while pind != len(pattern) or sind != len(source):
        # 1) check to see if we are at the end of the pattern (from the while
        # condition we know since we already checked to see if you were at the
        # end of the pattern and the source, then you know that if this is True,
        # then the pattern has ended, but the source has not)
        # if we reached the end of the pattern but not source then no match
        if pind == len(pattern):
            return None

        # 2) check to see if the current thing in the pattern is a %
        elif pattern[pind] == "%":
            # pattern has not ended: accumulate match
            accumulator = "" # a place to store the match
            pind += 1

            # keep accumulating while we haven't hit the end of the source
            while sind != len(source):
                # NOTE: The below break statement handles the trickiness of a %
                # at the end of a pattern, this same idea can also be handled
                # by removing the if/break below and replacing the above
                # `while sind != len(source)` check with this:
                # while sind != len(source) and (
                #     pattern[pind] != source[sind] if pind != len(pattern) else True):

                # stop accumulating if we aren't at the end of the pattern
                # and the pattern and source match up
                if pind != len(pattern) and pattern[pind] == source[sind]:
                    break

                accumulator += " " + source[sind]
                sind += 1

            result += [accumulator.strip()]

        # 3) if we reached the end of the source but not pattern then no match
        elif sind == len(source):
            return None

        # 4) check to see if the current thing in the pattern is an _
        elif pattern[pind] == "_":
            # neither has ended: add a singleton
            result += [source[sind].strip()]
            pind += 1
            sind += 1

        # 5) check to see if the current thing in the pattern is the same
        # as the current thing in the source
        elif pattern[pind] == source[sind]:
            # neither has ended and the words match, continue checking
            pind += 1
            sind += 1

        # 6) this will happen if none of the other conditions are met
        else:
            # neither has ended and the words do not match, no match
            return None

    return result