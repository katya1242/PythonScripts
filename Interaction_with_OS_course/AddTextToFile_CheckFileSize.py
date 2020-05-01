
def create_python_script(filename):
    file = open(filename)
    comments = "# Start of a new Python program"
    with open(filename, 'a') as file:
        file.write(comments + "\n")
        filesize = file.tell()
    return(filesize)

print(create_python_script("program.py"))

