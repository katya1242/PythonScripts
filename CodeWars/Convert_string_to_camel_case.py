# Complete the method/function so that it converts dash/underscore delimited words
# into camel casing. The first word within the output should be capitalized only if
# the original word was capitalized (known as Upper Camel Case, also often referred
# to as Pascal case).
#
# --------------------Examples
# to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"
#
# to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"

def to_camel_case(text):
    if len(text) > 0:
        s = text[0]
        arr = [text[i].upper() if text[i-1] == "_" or text[i-1] == "-" else text[i] for i in range(1, len(text)) ]
        return s + "".join(arr).replace("_", "").replace("-", "")
    return text


print(to_camel_case('')) #expected ''
print(to_camel_case("the_stealth_warrior")) #expected "theStealthWarrior"
print(to_camel_case("The-Stealth-Warrior")) #expected "TheStealthWarrior"
print(to_camel_case("A-B-C")) #expected "ABC"