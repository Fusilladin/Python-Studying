import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line)
# prints out the entire CSV csv_file

import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)  # skips the first row (header) and just prints out the rest of the rows of data

    for line in csv_reader:
        print(line[2])
# the [2] index prints out only the 2nd column in the file

####

import csv

with open('names.csv', 'r') as csv_file:  # open original file
    csv_reader = csv.reader(csv_file)  # creattin csv variable, and then reading it

    with open('new_names.csv', 'w') as new_file:  # opening a new file and then using a writer
        # delimiter will create the char that you want to use
        csv_writer = csv.writer(new_file, delimiter='-')

        for line in csv_reader:  # for each line the data - writing out a new line in the new file
            csv_writer.writerow(line)
# the [2] index prints out only the 2nd column in the file

# ouput is nothing, but it creates a new file

# when there is a dash in an email it puts the email into quotes as to not confuse that dash as a delimiter

####

('-')
(',')
('\t')  # tabs

####


with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)  # Makes each record column name become the key

    for line in csv_reader:
        print(line['email'])  # so you can search by the key only

####


with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name', 'email']  # Adding the fieldnames
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames,
                                    delimiter='\t')  # providing the fieldnames

        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)

####


with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name']  # leave out the ones you don't want
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']  # which line to delete
            csv_writer.writerow(line)
