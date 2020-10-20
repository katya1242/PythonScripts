# You will be given the lower and upper limits: the program will look for any prime number that exists between the lower limit to the upper limit (included).
#
# Your objective is to sum all the primes between the given limits.

def sum_primes(lower, upper):
    primes = []
    if lower > upper:
        return 0
    for i in range(lower, upper+1):
        test = isPrime(i, upper+1)
        if test == True and i != 1:
            primes.append(i)
    print(primes)
    return sum(primes)


def isPrime(number, upper):
    for i in range(2, upper):
        if number%i == 0 and number != i:
            return False
    return True

print(sum_primes(20, 4))