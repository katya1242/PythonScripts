# Your message is a string containing space separated words.
# You need to encrypt each word in the message using the following rules:
# The first letter needs to be converted to its ASCII code.
# The second letter needs to be switched with the last letter
# Keepin' it simple: There are no special characters in input.

# -----------------Examples----------------:
# encrypt_this("Hello") == "72olle"
# encrypt_this("good") == "103doo"
# encrypt_this("hello world") == "104olle 119drlo"

def encrypt_this(text):
    arr = text.split()
    new_str = []
    new_wrd = ""
    for word in arr:
        new_wrd = "".join([str(ord(word[i])) if i == 0 else word[-1] if i == 1 else word[1] if i == len(word) - 1 else word[i] for i in range(len(word))])
        new_str.append(new_wrd)
    return " ".join(new_str)

print(encrypt_this("The more he saw the less he spoke"))    #
print("expected: 84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp")