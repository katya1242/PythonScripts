def correct_polish_letters(st):
    dict_of_polish_letters = {'ą': 'a', 'ć': 'c', 'ę': 'e',
                              'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z'}
    for letter in st:
        if letter in dict_of_polish_letters:
            st = st.replace(letter, dict_of_polish_letters[letter])
    return st;

print(correct_polish_letters('Jędrzej Błądziński'))


def expression_matter(a, b, c):
    res1 = a * (b + c)
    res2 = a * b * c
    res3 = a + b * c
    res4 = (a + b) * c
    res5 = a + b + c

    max = 0;
    if (res1 >= max):
        max = res1
        print('1:' + str(max))
    if (res2 >= max):
        max = res2
        print('2:' + str(max))
    if (res3 >= max):
        max = res3
        print('3:'  + str(max))
    if (res4 >= max):
        max = res4
        print('4:'+  str(max))
    if (res5 >= max):
        max = res5
        print('5:' + str(max))

    return max

print(expression_matter(1, 1, 1))