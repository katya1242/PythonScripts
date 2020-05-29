def count_substring(string, sub_string):
    num = 0
    for i in range(0, len(string)):
        if string[i: i + len(sub_string)] == sub_string:
            num += 1
    return num

print(count_substring("FGTFGJFG", "FG"))