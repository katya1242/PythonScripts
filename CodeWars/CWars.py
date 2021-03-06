# Normally we have firstname, middle and the last name but there may be
# more than one word in a name like a South Indian one.
#
# Similar to those kinda names we need to initialize the names.
#
# See the pattern below:
#
#   initials('code wars') => returns C.Wars
#   initials('Barack Hussain obama') => returns B.H.Obama

def initials(name):
    return ".".join([el[0].title() if el != name.split()[-1] else el.title() for el in name.split()])

print(initials('Barack hussein obama'))