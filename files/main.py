# Do not modify these lines
__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

# Add your code after this line
import os
from zipfile import ZipFile

# Part 1


def clean_cache():
    path = r'C:\Users\Michael\Documents\Winc\Module 3\files\cache'  # Used absolute path. When using current directory i had trouble checking the answer with Wincpy
    isExist = os.path.exists(path)  # Check if cache folder exists
    if isExist is False:
        os.makedirs('cache')  # Make cache folder if it doesn't exist
    for f in os.listdir(path):
        os.remove(os.path.join(path, f))  # Clear the folder of all files
    print(isExist)

# Part 2


def cache_zip(zip_file_path, cache_dir_path):
    with ZipFile(zip_file_path, 'r') as f:
        f.extractall(cache_dir_path)  # Unpack zip file in the specified folder

# Part 3


def cached_files():
    dir_path = r'C:\Users\Michael\Documents\Winc\Module 3\files\cache'
    list_of_files = []
    for path in os.scandir(dir_path):
        if path.is_file():
            list_of_files.append(os.path.abspath(path))  # Add all files to the list of files found in the folder
    return list_of_files


# Part 4


def find_password(list_of_files):
    for file in list_of_files:  # Iterate through the list of files
        with open(file, 'r') as f:  # Open the iterated file and save it in f
            content = f.readlines()  # Read every line and save it in content
            for line in content:  # Iterate through every line of the file
                if ('password' or 'Password') in line:  # Look for a line with 'password' in it
                    print(f'Password found in file: {file}')
                    password = line[(line.find(' ')+1):-1]
                    return password


print(find_password(cached_files()))
