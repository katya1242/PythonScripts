# Input: String which consists of two positive numbers (doubles)
# and exactly one operator like +, -, * or / always between these
# numbers. The string is dirty, which means that there are different
# characters inside too, not only numbers and the operator. You have
# to combine all digits left and right, perhaps with "." inside
# (doubles), and to calculate the result which has to be rounded to an
# integer and converted to a string at the end.

def calculate_string(st):
    arr = [el for el in st if el.isnumeric() or el in '.+-*/']
    return str(round(eval("".join(arr))))

print(calculate_string("fsdfsd235???34.4554s4234df-sdfgf2g3h4j442"))