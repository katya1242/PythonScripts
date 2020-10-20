####If the array index is divisible by the first integer argument (NumOne), push the first string (StringOne) to the array.

#If the array index is divisible by the second integer argument (NumTwo), push the second string (StringTwo) to the array.

#If the array index is divisible by both the first and second integer arguments, push the concatanated strings to the array.

#If the array index is not divisible by either of the first and second integer arguments, push the index number to the array.

def fizz_buzz_custom(string_one = "Fizz", string_two = "Buzz", num_one = 3, num_two = 5):
    arr = list(range(1, 101))
    for i in range(len(arr)):
        if arr[i] % num_one == 0 and arr[i] % num_two == 0:
            arr[i] = string_one + string_two
        elif arr[i] % num_one == 0:
            arr[i] = string_one
        elif arr[i] % num_two == 0:
            arr[i] = string_two
    return arr

print(fizz_buzz_custom('Hey', 'There', 3, 5))
