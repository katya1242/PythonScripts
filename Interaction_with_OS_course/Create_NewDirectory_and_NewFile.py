import os


def new_directory(directory, filename):
    # Before creating a new directory, check to see if it already exists
    path = os.getcwd()
    full_Dir_Path = os.path.join(path, directory)
    if not os.path.isdir(directory):
        os.mkdir(full_Dir_Path)

    # Create the new file inside of the new directory
    full_File_Path = os.path.join(full_Dir_Path, filename)
    with open(full_File_Path, 'w') as file:
        pass
    # Return the list of files in the new directory

    dir_list = os.listdir(full_Dir_Path)
    return (dir_list)


print(new_directory("PythonPrograms", "script.py"))