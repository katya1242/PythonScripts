# Write a function, persistence, that takes in a positive parameter num and returns its
# multiplicative persistence, which is the number of times you must multiply the digits
# in num until you reach a single digit.

# persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                       # and 4 has only one digit.

def persistence(n):
    count = 0
    prod = 1
    while n >= 10:
        for i in str(n):
            prod *= int(i)
        n = prod
        prod = 1
        count += 1
    return count

print(persistence(39))