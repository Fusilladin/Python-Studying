# csv Notes

# import csv to read and write csv's
import csv

####

# create a csv_file object tp be used to pull when reading, put 'r' in there to read
with open('sales_data.csv', 'r') as csv_file:
    # create a csv_reader object to initiate the csv.reader() function that assumes commas(,)
    csv_reader = csv.reader(csv_file)

# when we print it out now it just shows that it is a file in memory, does not print the actual text
print(csv_reader)

####

# prints out each row of data with a list of it's values.
with open('sales_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line)

####

# To print out a certain column of data you can select the index. Indexes start at 0
with open('sales_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line[2])

####

# to print out the rows of data and exclude the first row (the headers) add in a next clause to iterate over it
with open('sales_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    for line in csv_reader:
        print(line[2])

####

# to write a new file:

# open initial file to be read
with open('sales_data.csv', 'r') as csv_file:
    # create a csv reader variable using the csv.reader method
    csv_reader = csv.reader(csv_file)

    # opening a new file to write into
    with open('new_names.csv', 'w') as new_file:
        # create a csv_writer variable using the csv.writer method. first variable is the object, and second is the delimiter
        csv_writer = csv.writer(new_file, delimiter='-')

        # for each line in the reader we write out a line in the new file
        for line in csv_reader:
            csv_writer.writerow(line)

# copy paste it to create a new file
with open('sales_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_names.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='-')

        for line in csv_reader:
            csv_writer.writerow(line)

####

# create a better delimiter - tabs
csv_writer = csv.writer(new_file, delimiter='\t')

####

# to read a csv file correctly with a unique delimiter put it into the reader method
with open('new_names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')

    for line in csv_reader:
        print(line)

####

# using the DictReader method you can see each column parsed out so you can more easily read the data
with open('new_names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter='\t')

    for line in csv_reader:
        print(line)

####

# print out the column of data you want by name instead of index
with open('new_names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter='\t')

    for line in csv_reader:
        print(line['Day'])

####

# Write a file using the DictWriter method
with open('new_names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter='\t')

    with open('new_names.csv', 'w') as new_file:
        # add a new line adding in the column names
        fieldnames = ['Date', 'Age_group']
        # change to DictWriter and add in the fieldnames
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
        # option to write out the headers if you want them - typically you do
        csv_writer.writeheader()

        # loop through the lines of the original file
        for line in csv_reader:
            csv_writer.writerow(line)

####

        # to delete a column of data use the del function at the end
        for line in csv_reader:
            del line['Date']
            csv_writer.writerow(line)
