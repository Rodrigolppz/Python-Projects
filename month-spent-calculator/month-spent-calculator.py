# 1 - I need Python to read the .csv file
# 2 - I need Python to pick only the right columns and rows to read
# 3 - I need Python to sum the total value for all rows in one column, then do it for the other columns and store the total money spent of each column.
# 4 - I need Python to print the result and tells me in which column i spent the most during the month.

import csv
import os 

# Using os lib to define the path for my test.csv file

current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, 'test.csv')

# opening the file 

with open(csv_path) as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
