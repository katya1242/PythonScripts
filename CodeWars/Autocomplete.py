#The autocomplete function will take in an input string and a dictionary array and
# return the values from the dictionary that start with the input string. If there
# are more than 5 matches, restrict your output to the first 5 results. If there are
# no matches, return an empty array.

def autocomplete(input_, dictionary):
    input_ = "".join([el for el in input_ if el.isalpha()])
    return [el for el in dictionary if el.lower().startswith(input_.lower())][:5]