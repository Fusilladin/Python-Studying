import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv

with open('sales_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line)

csv_reader.head()
csv_reader.shape
