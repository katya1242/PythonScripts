#   accum("abcd") -> "A-Bb-Ccc-Dddd"
#   accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
#   accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.

def accum(s):
    my_list = []
    for i, letter in enumerate(s):
      my_list.append((letter * (i + 1)).title())
    return "-".join(my_list)

print(accum("ZpglnRxqenU"))