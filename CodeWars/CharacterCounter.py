def validate_word(word):
    count = word.lower().count(word[0].lower())
    new_set = set(word.lower())
    for el in new_set:
        count2 = word.lower().count(el)
        if count2 != count:
            return False
    return True

print(validate_word("abcabc"))
print(validate_word("AbcabcC"))