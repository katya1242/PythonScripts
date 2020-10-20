#For a given string s find the character c (or C) with longest consecutive repetition
# and return:
#      (c, l)
# where l (or L) is the length of the repetition.
# If there are two or more characters with the same l return the first in order of appearance.
# For empty string return:
#       ('', 0)

def longest_repetition(chars):
    if chars == "":
        return ("", 0)
    str = chars[0]
    for i in range(1, len(chars)):
        if chars[i] != chars[i-1]:
            str += " " + chars[i]
        else:
            str += chars[i]
    len_lst = [len(el) for el in str.split()]
    char_lst = [el[0] for el in str.split()]
    return (char_lst[len_lst.index(max(len_lst))], max(len_lst))

#tests
print(longest_repetition("aaaabb"))  #expected ('a', 4)
print(longest_repetition("bbbaaabaaaa"))  #expected ('a', 4)
print(longest_repetition("cbdeuuu900"))  #expected ('u', 3)
print(longest_repetition("abbbbb"))  #expected ('b', 5)
print(longest_repetition("aabb"))  #expected ('a', 2)
print(longest_repetition("ba"))  #expected ('b', 1)
print(longest_repetition(""))  #expected ('', 0)
