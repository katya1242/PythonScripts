#Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"
#Your task is to process a string with "#" symbols.

#-------------Examples
#       "abc#d##c"      ==>  "ac"
#       "abc##d######"  ==>  ""
#       "#######"       ==>  ""
#       ""              ==>  ""


def clean_string(s):
    res = []
    for el in s:
        if el != "#":
            res.append(el)
        elif len(res) > 0:
            res.pop()
    return "".join(res)

print(clean_string("a#bghg#"))