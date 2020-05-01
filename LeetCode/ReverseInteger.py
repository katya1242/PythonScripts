class Solution:
    def reverse(number):
        my_list = []

        if abs(number) < 9:
            return number
        else:
            for i in str(number):
                if i != '-':
                    my_list.append(i)
            my_list.reverse()
            separator = ""
            new_number = str(separator.join(my_list))
            result = new_number.lstrip("0")
            if int(result) <= -2**31 or int(result) >= 2**31-1:
                return 0
            if number < 0:
                return "-" + result
            else: return result

    print(reverse(-1534236469))
