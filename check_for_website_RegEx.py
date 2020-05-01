import re
def check_web_address(text):
  pattern = r"^[a-zA-Z0-9][a-zA-Z0-9-_\+]*[\.a-zA-Z]*$"
  result = re.search(pattern, text)
  print(result)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True

#The check_time function checks for the time format of a 12-hour clock, as follows:
# the hour is between 1 and 12, with no leading zero, followed by a colon, then minutes
# between 00 and 59, then an optional space, and then AM or PM, in upper or lower case.

def check_time(text):
  pattern = r"[1-9][0-2]?[:][0-5][0-9][ ]?[AM|PM|am|pm]"
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False