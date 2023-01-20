import os


def print_directories(directory_list):
    i = 0
    print("Sr. No. \t Directory")
    print("-" * 40)
    for directory in directory_list:
        print(i, "\t\t", directory)
        i += 1


def print_directory_path_and_content(path):
    print("The current working directory is:", path)
    # Directories present in a specic path
    print_directories(os.listdir(path))


# Print Current
path = os.getcwd()
print_directory_path_and_content(path)
# Make Directory using mkdir
directory_name = input("\nEnter Directory Name to be created: ")
os.mkdir(os.path.join(path, directory_name))
# Print after creating Directories
print_directory_path_and_content(os.getcwd())
# Change Directory to the created one
os.chdir(directory_name)
# Print after changing Directories
print_directory_path_and_content(os.getcwd())
path = os.getcwd()
# Make Directory using makedirs
path += r"/a/b/c"
os.makedirs(path)
# Print after creating Directories
print_directory_path_and_content(os.getcwd())
# Change Directory to the created one
os.chdir(r"a/b/c")
# Print after changing Directories
print_directory_path_and_content(os.getcwd())
os.chdir(r"../../..")
# Print after changing Directories
print_directory_path_and_content(os.getcwd())
path = os.getcwd()
path += r"/a/b/c"
# Remove directory
os.rmdir(path)
# Print after changing Directories
print_directory_path_and_content(os.getcwd())
