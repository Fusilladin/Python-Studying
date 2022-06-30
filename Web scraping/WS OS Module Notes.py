# OS Module

import os

# print(dir(os))  # See all of the OS Module options
print(os.getcwd())  # See where the file location is

os.chdir(r"C:\Users\jgodin\Pictures\AB Data\Templates\Studying\python\Web scraping")  # chooses the file location # noqa

os.mkdir('OS-Demo-2')  # Create a new folder
os.makedirs('OS-Demo-2/Sub-Dir-1')  # Able to make multiple sub-folers #####

os.rmdir('OS-Demo-2')  # Delete a folder ####
os.removedirs('OS-Demo-2/Sub-Dir-1')  # Will delete intermediary folders too

os.rename('WS2.PY', 'WS2.py')  # Rename a folder
os.removedirs('OS-Demo-2/Sub-Dir-1')  # Will delete intermediary folders too

# print(os.getcwd())  # naviagte to a new folder
print(os.listdir())  # Shows list directory // files and folders here

#  from datetime import datetime
print(os.getcwd())

mod_time = os.stat('WS2.PY').st_mtime  # details/properties on a file
print(datetime.fromtimestamp(mod_time))

# print(os.listdir())

#####

os.chdir(r"C:\Users\jgodin\Pictures\AB Data\Templates\Studying\python\Web scraping")

# Walk method. Will print out all of the information in all of the directories selected in order.
for dirpath, dirnames, filenames in os.walk(r"C:\Users\jgodin\Pictures\AB Data\Templates\Studying\python\Web scraping")

print('Current Path:', dirpath)
print('Directories:', dirnames)
print('Files:', filenames)
print()  # Can use the search method to go through and find what you are looking for

#######

os.chdir(r"C:\Users\jgodin\Pictures\AB Data\Templates\Studying\python\Web scraping")

print(os.environ.get('HOME'))  # Helps create a new file in the home area
file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)  # helps create a path where you don't have to worry about the correct backslashes for simplicity

####

with open(file_path, 'w') as f:
    f.wte  # Create a file

####

print(os.path.basename('/tmp/text.txt'))  # Creates a temp file
print(os.path.dirname('/tmp/text.txt'))
print(os.path.split('/tmp/text.txt'))  # Splits them into 2 strs

print(os.path.exists('/tmp/text.txt'))  # Check if it is there
print(os.path.isdir('/tmp/text.txt'))  # Check if directory
print(os.path.isfile('/tmp/text.txt'))  # Check if file

print(os.path.splitext('/tmp/text.txt'))  # Split into strings

####

print(dir(os.path))  # shows all of the directory files

####

with open('test.txt', 'r') as rf:
    with open('test.txt', 'w') as wf:
        for line in rf:
            wf.write(line)  # will create a file. For each line in original file re-write it into new file

# Will create a copy text file

####

with open('pic1.jpg', 'rb') as rf:
    with open('pic2.jpg', 'wb') as wf:
        for line in rf:
            # adding the b means you are wokring with the bytes of the photo and this is how to make a copy of it
            wf.write(line)

####

with open('pic1.jpg', 'rb') as rf:
    with open('pic2.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
            # will create exact copy of original
