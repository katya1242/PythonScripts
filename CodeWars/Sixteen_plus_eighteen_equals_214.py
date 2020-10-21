# For this Kata you will have to forget how to add two numbers together.
# In simple terms, our method does not like the principle of carrying over
# numbers and just writes down every number it calculates :-)
# You may assume both integers are positive integers
# ------------------Examples-------------:
#         test.assert_equals(add(16,18), 214)
#         test.assert_equals(add(26,39), 515)
#         test.assert_equals(add(122,81), 1103)

def add(num1, num2):
    num1 = str(num1)
    num2 = str(num2)

    max_len = max(len(num1), len(num2))
    num1 = num1.rjust(max_len, "0")
    num2 = num2.rjust(max_len, "0")
    res = []
    for i in range(max_len):
        res.append(int(num1[i]) + int(num2[i]))
    return int("".join([str(el) for el in res]))