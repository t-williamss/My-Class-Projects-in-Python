# Important variables:
#     movie_db: list of 4-tuples (imported from movies.py)
#     pa_list: list of pattern-action pairs (queries)
#       pattern - strings with % and _ (not consecutive)
#       action  - return list of strings

# THINGS TO ASK THE MOVIE CHAT BOT:
# what movies were made in _ (must be date, because we don't have location)
# what movies were made between _ and _
# what movies were made before _
# what movies were made after _
# who directed %
# who was the director of %
# what movies were directed by %
# who acted in %
# when was % made
# in what movies did % appear
# bye

#  Include the movie database, named movie_db
from movies import movie_db
from match import match
from typing import List, Tuple, Callable, Any

# Below are a set of actions. Each takes a list argument and returns a list of
# answers according to the action and the argument. It is important that each
# function returns a list of the answer(s) and not just the answer itself.

# The projection functions, that give us access
# to certain parts of a "movie" (a tuple)
def get_title(movie: Tuple[str, str, int, List[str]])    -> str:       return movie[0]
def get_director(movie: Tuple[str, str, int, List[str]]) -> str:       return movie[1]
def get_year(movie: Tuple[str, str, int, List[str]])     -> int:       return movie[2]
def get_actors(movie: Tuple[str, str, int, List[str]])   -> List[str]: return movie[3]

# imagine someone tells chatbot 
# source: "what movies were made in 1978?" 
# pattern:"What movies were made in _"
# match(pattern , source) -> ["1978"]
# action I want to take is title_by_year
####That is becuase I want to return a list of all the movies made in the year 1978 
def title_by_year(matches: List[str]) -> List[str]:
    """Finds all movies made in the passed in year

    Args:
        matches - a list of 1 string, just the year. Note that this year is
            passed as a string and should be converted to an int

    Returns:
        a list of movie titles made in the passed in year
    """
    yr = int(matches[0])
    def movie_made_in_year(movie: Tuple[str, str, int, List[str]]) -> bool:
        return yr == get_year(movie)
    mvs = list(filter(movie_made_in_year, movie_db))
    titles = list(map(get_title, mvs))
    return titles  


assert title_by_year(["1974"]) == ['amarcord', 'chinatown'], "failed title_by_year test"

def title_by_year_range(matches: List[str]) -> List[str]:
    """Finds all movies made in the passed in year range

    Args:
        matches - a list of 2 strings, the year beginning the range and the year
            ending the range. For example, to get movies from 1991-1994 matches
            would look like this - ["1991", "1994"] Note that these years are
            passed as strings and should be converted to ints.

    Returns:
        a list of movie titles made during those years, inclusive (meaning it
        if you pass in ["1991", "1994"] you will get movies made in 1991, 1992,
        1993 and 1994)
    """
    yr_low = int(matches[0])
    yr_hi = int(matches[1])
    def movie_made_in_year_rng(movie: Tuple[str, str, int, List[str]]) -> bool:
        return yr_low <= get_year(movie) <= yr_hi
    mvs = list(filter(movie_made_in_year_rng, movie_db))
    titles = list(map(get_title, mvs))
    return titles 

assert title_by_year_range(["1970", "1972"]) == ['the godfather', 'johnny got his gun'], "failed title_by_year_range test"

def title_before_year(matches: List[str]) -> List[str]:
    """Finds all movies made before the passed in year

    Args:
        matches - a list of 1 string, just the year. Note that this year is
            passed as a string and should be converted to an int

    Returns:
        a list of movie titles made before the passed in year
    """
    yr = int(matches[0])
    def movie_made_in_year(movie: Tuple[str, str, int, List[str]]) -> bool:
        return yr > get_year(movie) 
    mvs = list(filter(movie_made_in_year, movie_db))
    titles = list(map(get_title, mvs))
    return titles

assert title_before_year(["1950"]) == ['casablanca', 'citizen kane', 'gone with the wind', 'metropolis'], "failed title_before_year test"

def title_after_year(matches: List[str]) -> List[str]:
    """Finds all movies made after the passed in year

    Args:
        matches - a list of 1 string, just the year. Note that this year is
            passed as a string and should be converted to an int

    Returns:
        a list of movie titles made after the passed in year
    """
    yr = int(matches[0])
    def movie_made_in_year(movie: Tuple[str, str, int, List[str]]) -> bool:
        return yr < get_year(movie) 
    mvs = list(filter(movie_made_in_year, movie_db))
    titles = list(map(get_title, mvs))
    return titles

assert title_after_year(["1990"]) == ['boyz n the hood', 'dead again', 'the crying game', 'flirting', 'malcolm x'], "failed title_after_year test"

def director_by_title(matches: List[str]) -> List[str]:
    """Finds director of movie based on title

    Args:
        matches - a list of 1 string, just the title

    Returns:
        a list of 1 string, the director of the movie
    """
    title = str(matches[0])
    def movie_by_director(movie: Tuple[str, str, int, List[str]]) -> bool:
        return title == get_title(movie)
    mvs = list(filter(movie_by_director, movie_db))
    directors = list(map(get_director, mvs))
    return directors

assert director_by_title(["jaws"]) == ['steven spielberg'], "failed director_by_title test"

def title_by_director(matches: List[str]) -> List[str]:
    """Finds movies directed by the passed in director

    Args:
        matches - a list of 1 string, just the director

    Returns:
        a list of movies titles directed by the passed in director
    """
    director = str(matches[0])
    def movie_by_director_title(movie: Tuple[str, str, int, List[str]]) -> bool:
        return director == get_director(movie)
    mvs = list(filter(movie_by_director_title, movie_db))
    titles = list(map(get_title, mvs))
    return titles

assert title_by_director(["steven spielberg"]) == ['jaws'], "failed title_by_director test"

def actors_by_title(matches: List[str]) -> List[str]:
    """Finds actors who acted in the passed in movie title

    Args:
        matches - a list of 1 string, just the movie title

    Returns:
        a list of actors who acted in the passed in title
    """
    title = str(matches[0])
    def actors_by_movie(movie: Tuple[str, str, int, List[str]]) -> bool:
        return title == get_title(movie)
    mvs = list(filter(actors_by_movie, movie_db))
    actors = list(map(get_actors, mvs))
    return actors[0]


assert actors_by_title(["jaws"]) == ['roy scheider', 'robert shaw', 'richard dreyfuss', 'lorraine gary', 'murray hamilton'], "failed actors_by_title test"

def actors_by_year(matches: List[str]) -> List[str]:
    """Finds actors who acted in the passed in year

    Args:
       matches - a list of 1 string, just the year. Note that this year is
            # passed as a string and should be converted to an int

    #Returns:
        a list of actors who acted in the passed in year
    """ 
    yr = int(matches[0])
    def actors_by_movie_year(movie: Tuple[str, str, int, List[str]]) -> bool:
        return yr == get_year(movie)
    mvs = list(filter(actors_by_movie_year, movie_db))
    actors = list(map(get_actors, mvs))
    return actors[0]

assert actors_by_year(["1974"]) == ['magali noel', 'bruno zanin', 'pupella maggio','armando drancia'], "failed actors_by_year test"

def year_by_title(matches: List[str]) -> List[int]:
    """Finds year of passed in movie title
    Args:
        matches - a list of 1 string, just the movie title
    Returns:
        a list of actors who acted in the passed in title
    """
    title = str(matches[0])
    def year_by_movie(movie: Tuple[str, str, int, List[str]]) -> bool:
        return title == get_title(movie)
    mvs = list(filter(year_by_movie, movie_db))
    year = list(map(get_year, mvs))
    return year

assert year_by_title(["jaws"]) == [1975], "failed year_by_title test"

def title_by_actor(matches: List[str]) -> List[str]:
    """Finds titles of all movies that the given actor was in

    Args:
        matches - a list of 1 string, just the movie title

    Returns:
        a list of actors who acted in the passed in title
    """
    actor = str(matches[0])
    def movie_by_actor(movie: Tuple[str, str, int, List[str]]) -> bool:
        return actor in get_actors(movie)
    mvs = list(filter(movie_by_actor, movie_db))
    titles = list(map(get_title, mvs))
    return titles

assert title_by_actor(["orson welles"]) == ['citizen kane', 'othello'], "failed title_by_actor test"

# dummy argument is ignored and doesn't matter
def bye_action(dummy: List[str]) -> None: raise KeyboardInterrupt

# The pattern-action list for the natural language query system
# A list of tuples of pattern and action
# It must be declared here, after all of the function definitions
pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("what movies were made in _"),            title_by_year),
    (str.split("what movies were made between _ and _"), title_by_year_range),
    (str.split("what movies were made before _"),        title_before_year),
    (str.split("what movies were made after _"),         title_after_year),
    (str.split("who acted in year _"),                   actors_by_year),
    (str.split("who directed %"),                        director_by_title),
    (str.split("who was the director of %"),             director_by_title),
    (str.split("what movies were directed by %"),        title_by_director),
    (str.split("who acted in %"),                        actors_by_title),
    (str.split("when was % made"),                       year_by_title),
    (str.split("in what movies did % appear"),           title_by_actor),
    (["bye"],                                            bye_action)
]
# search pa list 
   #for each pattern action pair if we hae a match call on the corresponding action passing  it our result from match
   # if i never matched 
      # i dont understand 
    # elif we have no answers 
      # no answer 
    #else 
    # our answers 
   # elif we have no answers 
   # no anaswers 
   # else 
   # our answers 

def search_pa_list(src: List[str]) -> List[str]:
    """Takes source, finds matching pattern and calls corresponding action. If it
    finds a match but has no answers it returns ["No answers"]. If it finds no match
    it returns ["I don't understand"].

    Args:
        source - a phrase represented as a list of words (strings)

    Returns:
        a list of answers. Will be ["I don't understand"] if it finds
        no matches and ["No answers"] if it finds a match but no answers
    """
    for p in pa_list:
        result = match(p[0], src)
        if result != None:
            answer = p[1](result) #function(arg)
            if len(answer) == 0:
                return ["No answers"]
            else: return answer 
    return ["I don't understand"] 
    


        


assert search_pa_list(["hi", "there"]) == ["I don't understand"], "failed search_pa_list test 1"
assert search_pa_list(["who", "directed", "jaws"]) == ['steven spielberg'], "failed search_pa_list test 2"
assert search_pa_list(["what", "movies", "were", "made", "in", "2020"]) == ['No answers'], "failed search_pa_list test 3"
assert search_pa_list(["who", "acted","in", "year", "1974"]) == ['magali noel', 'bruno zanin', 'pupella maggio','armando drancia'], "failed search_pa_list test 4"

def query_loop() -> None:
    """The simple query loop. The try/except structure is to catch Ctrl-C or
    Ctrl-D characters and exit gracefully.
    """
    print("Welcome to the movie database!\n")
    while True:
        try:
            print()
            query = input("Your query? ").replace("?", "").lower().split()
            answers = search_pa_list(query)
            for ans in answers: print(ans)

        except (KeyboardInterrupt,EOFError):
            break

    print("\nSo long!\n")

# uncomment the following line once you've written all of your code and are
# ready to try it out. Before running the following line, you should make sure
# that your code passes the existing asserts.
query_loop()