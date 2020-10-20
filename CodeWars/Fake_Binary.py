def fake_bin(x):
    list1 = list(x)
    for i, c in enumerate(list1):
        if int(c) < 5:
            list1[i] = "0"
        if int(c) >= 5:
            list1[i] = "1"
    return ''.join(list1)

print(fake_bin("45385593107843568"))