# Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter.
# Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.
# If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is positive.
#   findNextSquare(121) --> returns 144
#   findNextSquare(625) --> returns 676
#   findNextSquare(114) --> returns -1 since 114 is not a perfect

import math
def find_next_square(sq):
    return (math.sqrt(sq) + 1)**2 if int(math.sqrt(sq))**2 == sq else -1
