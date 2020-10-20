#   Given two integers a and b, which can be positive or negative,
#   find the sum of all the numbers between including them too and return it.
#   If the two numbers are equal return a or b.
#   Note: a and b are not ordered!

def get_sum(a,b):
    if a == b:
        return a
    c = min(a, b)
    d = max(a, b)
    sum = c
    while c < d:
        sum += c + 1
        c += 1
    return sum

print(get_sum(0,-1))