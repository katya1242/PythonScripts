# You are given a string and your task is to swap cases.
# In other words, convert all lowercase letters to uppercase letters and vice versa.

"""For Example:
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  """

def swap_case(s):
    new_string = ''
    for character in s:
        if character.islower() is True:
            new_letter = character.upper()
            new_string = new_string + new_letter
        else:
            new_letter = character.lower()
            new_string = new_string + new_letter
    return new_string

s = "jhjhjGGH KJKJKJjhikoi!!!"
result = swap_case(s)
print(result)