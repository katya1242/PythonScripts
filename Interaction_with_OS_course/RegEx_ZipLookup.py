#Fill in the code to check if the text passed includes a possible U.S. zip code,
# formatted as follows: exactly 5 digits, and sometimes, but not always,
# followed by a dash with 4 more digits. The zip code needs to be preceded by at
# least one space, and cannot be at the start of the text.

import re
def check_zip_code(text):
  result = re.search(r".*[ ][0-9][0-9][0-9][0-9][0-9]|[0-9][0-9][0-9][0-9][0-9][-][0-9][0-9][0-9][0-9]", text)
  return result != None

print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
print(check_zip_code("90210 is a TV show")) # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False

#Fill in the code to check if the text passed looks like a standard sentence, meaning that it starts
# with an uppercase letter, followed by at least some lowercase letters or a space, and ends with a period,
# question mark, or exclamation point.

def check_sentence(text):
  result = re.search(r"^[A-Z][a-z ].*[.?!]$", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True