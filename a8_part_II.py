# some python libraries we'll be using
import re, string, calendar
from wikipedia import page
from bs4 import BeautifulSoup

from typing import List, Match

# Assignment 8 Part II

def get_page_html(title: str) -> str:
  """Gets html of a wikipedia page

  Args:
    title - title of the page

  Returns:
    html of the page
  """
  return page(title).html()

def get_first_infobox_text(html: str) -> str:
  """Gets first infobox html from a Wikipedia page (summary box)

  Args:
    html - the full html of the page

  Returns:
    html of just the first infobox
  """
  soup = BeautifulSoup(html, 'html.parser')
  results = soup.find_all(class_ = 'infobox')

  if not results:
    raise LookupError('Page has no infobox')

  return results[0].text

def clean_text(text: str) -> str:
  """Cleans given text removing non-ASCII characters and duplicate spaces & newlines

  Args:
    text - text to clean

  Returns:
    cleaned text
  """
  only_ascii = ''.join([char if char in string.printable else ' ' for char in text])
  no_dup_spaces = re.sub(' +', ' ', only_ascii)
  no_dup_newlines = re.sub('\n+', '\n', no_dup_spaces)
  return no_dup_newlines

def get_match(text: str, pattern: str,
    error_text: str = "Page doesn't appear to have the property you're expecting") -> Match:
  """Finds regex matches for a pattern

  Args:
    text - text to search within
    pattern - pattern to attempt to find within text
    error_text - text to display if pattern fails to match

  Returns:
    text that matches
  """
  p = re.compile(pattern, re.DOTALL | re.IGNORECASE)
  match = p.search(text)

  if not match:
    raise AttributeError(error_text)

  return match

def format_birth(date: str, name: str) -> str:
  """Cleanly formats a given date string

  Args:
    date - the date string to format

  Returns:
    formatted date
  """
  year, raw_month, day = date.split('-')
  month = calendar.month_name[int(raw_month)]
  return f'{name}: born {month} {day}, {year}'


def get_planet_radius(planet_name: str) -> str:
  """Gets the radius of the given planet

  Args:
    planet_name - name of the planet to get radius of

  Returns:
    radius of the given planet
  """
  infobox_text = clean_text(get_first_infobox_text(get_page_html(planet_name)))
  # TODO: fill this in
  pattern = "Polar[\s]Radius[\s]+(?P<radius>(([\d]+.[\d]+)))" #how to code it disregarding the commas and number of digits 
  error_text = "Page infobox has no polar radius information"
  match = get_match(infobox_text, pattern, error_text)
  return match.group('radius')

print('\n<<<<<<<<<<<<<< Testing Planet Radius >>>>>>>>>>>>>>')
print(f'Mars has a polar radius of {get_planet_radius("Mars")}km') # should be 3,376.2
print(f'Earth has a polar radius of {get_planet_radius("Earth")}km') # should be 6356.8
print(f'Jupiter has a polar radius of {get_planet_radius("Jupiter")}km') # should be 66,854
print(f'Saturn has a polar radius of {get_planet_radius("Saturn")}km') # should be 54,364

# uncomment below lines for tests once you think you're getting the right output
print('\n<<<< Running asserts, this might take a sec >>>>')
assert get_planet_radius("Mars") == "3376.2", "Incorrect radius for Mars"
assert get_planet_radius("Earth") == "6356.8", "Incorrect radius for Earth"
assert get_planet_radius("Jupiter") == "66,854", "Incorrect radius for Jupiter"
assert get_planet_radius("Saturn") == "54,364", "Incorrect radius for Saturn"
print('\n<<<< Planet radius tests passed >>>>')

def get_birth_date(name: str) -> str:
  """Gets birth date of the given person

  Args:
    name - name of the person

  Returns:
    birth date of the given person
  """
  infobox_text = clean_text(get_first_infobox_text(get_page_html(name)))
  # TODO: fill this in
  pattern = "(?P<birth>([\d]+-[\d]+-[\d]+))"
  error_text = ("Page infobox has no birth information "
    "(to be more specific none in xxxx-xx-xx format)")
  match = get_match(infobox_text, pattern, error_text)
  return match.group('birth')

print('\n<<<<<<<<<<<<<< Testing Birth Dates >>>>>>>>>>>>>>')
print(format_birth(get_birth_date("Grace Hopper"), "Grace Hopper")) # should be 1906-12-09
print(format_birth(get_birth_date("Alan Turing"), "Alan Turing")) # should be 1912-06-23
print(format_birth(get_birth_date("Tim Berners-Lee"),  "Tim Berners-Lee")) # should be 1955-06-08
print(format_birth(get_birth_date("Anita Borg"), "Anita Borg")) # should be 1949-01-17

# uncomment below lines for tests once you think you're getting the right output
# print('\n<<<< Running asserts, this might take a sec >>>>')
assert get_birth_date("Grace Hopper") == "1906-12-09", "Incorrect birth date for Grace Hopper"
assert get_birth_date("Alan Turing") == "1912-06-23", "Incorrect birth date for Alan Turing"
assert get_birth_date("Tim Berners-Lee") == "1955-06-08", "Incorrect birth date for Tim Berners-Lee"
assert get_birth_date("Anita Borg") == "1949-01-17", "Incorrect birth date for Anita Borg"
print('\n<<<< Birth date tests passed >>>>')

print('\n<<<< All tests passed! >>>>')
