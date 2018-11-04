import re
# Assignment 8 Part I
# In each of the problems below the first parameter to re.compile is "REPLACE ME"
# Your job is to replace this text with a regular expression that behaves as
# described by the comment and accompanying prints/tests

# problem 1
# should extract a match where the first group is the month, the second group
# the day and the third group the year
print('<<<<< Date Problem >>>>>\n')
date_string = "January 24, 1985"  
pat = re.compile("(?P<month>[a-zA-Z]+)\s(?P<day>[0-9]+)\,\s(?P<year>[0-9]+)", re.IGNORECASE)
mat = pat.match(date_string)
# uncomment the following prints to see results and asserts to test
print(f"month is: {mat.group(1)}!") # should print "month is: January"  (?P<areacode>([0-9]+))\)
print(f"day is: {mat.group(2)}!")   # should print "day is: 24"
print(f"year is: {mat.group(3)}!")  # should print "year is: 1985"
assert mat.group(1) == 'January', "Incorrect month"
assert mat.group(2) == '24', "Incorrect day"
assert mat.group(3) == '1985', "Incorrect year"
print('\n<<<< Date extraction tests passed >>>>')

# problem 2
# should extract a match where the first group is the number, the second the
# street, the third the city, the fourth the state and the fifth the zip code
print('<<<<< Address Problem >>>>>\n')
address_string = "2133 Sheridan Road\nEvanston, IL 60208" 
pat = re.compile("(?P<number>[0-9]+)\s+(?P<street>[a-zA-Z]+\s[a-zA-Z]+)\W(?P<city>[a-zA-Z]+)\,\s+(?P<state>[A-Z]+)\s+(?P<zip>[0-9]+)", re.IGNORECASE)
mat = pat.match(address_string)
# uncomment the following prints to see results and asserts to test
print(f'number is: {mat.group("number")}!') # should print "number is: 2133"
print(f'street is: {mat.group("street")}!') # should print "street is: Sheridan Road"
print(f'city is: {mat.group("city")}!')     # should print "city is: Evanston"
print(f'state is: {mat.group("state")}!')   # should print "state is: IL"
print(f'zip is: {mat.group("zip")}!')       # should print "zip is: 60208"
assert mat.group('number') == '2133', "Incorrect address number"
assert mat.group('street') == 'Sheridan Road', "Incorrect street"
assert mat.group('city') == 'Evanston', "Incorrect city"
assert mat.group('state') == 'IL', "Incorrect state"
assert mat.group('zip') == '60208', "Incorrect zip"
print('\n<<<< Address extraction tests passed >>>>')

# problem 3
print('<<<<< Hashtag Problem >>>>>\n')
# should match all hashtags
tweet_string = "hi everyone! #cs #python #nu #wildcats"
pat = re.compile("[a-zA-Z]+\s[a-zA-Z]+.\s+(?P<hashtags>.[a-zA-Z]+\s.[a-z]+\s.[a-z]+\s.[a-z]+)", re.IGNORECASE)
mats = pat.findall(tweet_string)
# uncomment the following prints to see results and asserts to test
print(f"hashtags are: {mats}") # should be ['cs', 'python', 'nu', 'wildcats']"
assert mats == ['cs', 'python', 'nu', 'wildcats'], "Incorrect hashtags"
print('\n<<<< Hashtag extraction tests passed >>>>')

print('\n<<<< All tests passed! >>>>')