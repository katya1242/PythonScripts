#Write a function that will return the count of distinct case-insensitive alphabetic characters
# and numeric digits that occur more than once in the input string. The input string can be
# assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

######  Example
#       "abcde" -> 0 # no characters repeats more than once
#       "aabbcde" -> 2 # 'a' and 'b'
#       "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
#       "indivisibility" -> 1 # 'i' occurs six times
#       "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
#       "aA11" -> 2 # 'a' and '1'
#       "ABBA" -> 2 # 'A' and 'B' each occur twice

def duplicate_count(text):
    text.lower()
    dic = {}
    count = 1
    res = 0
    for letter in text:
        if letter in dic:
            count += 1
            dic[letter] = count
        else:
            dic[letter] = 1
    print(dic)
    for key in dic:
        if dic.get(key) > 1:
            res += 1
    return res

print(duplicate_count("Indivisibilities"))