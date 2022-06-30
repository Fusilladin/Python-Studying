import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name', 'email']  # Adding the fieldnames
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames,
                                    delimiter='\t')  # providing the fieldnames

        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)
