# File Objects

f = open('test.txt', 'r')  # reading (default is reading)
f = open('txt.py', 'w')  # Writing
f = open('txt.py', 'a')  # Appending
f = open('txt.py', 'r+')  # Read and write

####

f = open('txt.py', 'r')
print(f.name)  # print the name of file
f.close()  # if open a file you must close it

print(f.mode)  # shows the mode of the file (reading, writing)

####

with open('test.txt', 'r') as f:  # context manager to work with something inside of the block
    pass
# will automaticaly close the file
# automatically close file is there are exceptions

print(f.mode())  # if open a file you must close it
print(f.closed())  # will show if the file is open or not

####

with open('test.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)  # shows contents of file

with open('test.txt', 'r') as f:
    f_contents = f.readlines()
    print(f_contents)  # shows every new line

with open('test.txt', 'r') as f:
    f_contents = f.readline()
    print(f_contents)  # shows first line of the file

####

with open('test.txt', 'r') as f:
    f_contents = f.readline()
    print(f_contents)  # every time is will read the next line
    f_contents = f.readline()
    print(f_contents, end='')  # removes additional line in between each record

# <----- this one is useful

with open('test.txt', 'r') as f:

    for line in f:
        print(line, end='')  # prints all of the lines out nicely

with open('test.txt', 'r') as f:

    f_contents = f.read(100)
    print(f_contents, end='')  # prints first 100 characters
    f_contents = f.read(100)
    print(f_contents, end='')  # will do the next 100 characters

####

with open('test.txt', 'r') as f:

    size_to_read = 100
    f_contents = f.read(size_to_read)
    print(f_contents, end='')

    while len(f_contents) > 0:
        print(f_contents, end='')
        f_contents = f.read(size_to_read)
# this will print the characters in a loop until there are none left

with open('test.txt', 'r') as f:

    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents, end='')

    while len(f_contents) > 0:
        print(f_contents, end='*')
        f_contents = f.read(size_to_read)
# This will print everything and drop a * every 10 characters

####

with open('test.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f.tell())
# prints the number of loops that it will go through

####

with open('test.txt', 'r') as f:
    size_to_read = 10

    f_contents = f.read(size_to_read)
    print(f_contents, end='')

    f.seek(0)  # will change the position before continuing the loop

    f_contents = f.read(size_to_read)
    print(f_contents)

####
