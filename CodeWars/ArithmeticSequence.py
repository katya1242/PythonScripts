#   arithmetic_sequence_sum(2, 3, 5) should return 40:

#   1     2        3          4            5
#   a + (a+r) + (a+r+r) + (a+r+r+r) + (a+r+r+r+r)
#   2 + (2+3) + (2+3+3) + (2+3+3+3) + (2+3+3+3+3) = 40

def arithmetic_sequence_sum(a, r, n):
    i = 1
    sum = a
    while i < n:
        sum += a + r * i
        i += 1
    return sum

print(arithmetic_sequence_sum(3, 2, 20))

