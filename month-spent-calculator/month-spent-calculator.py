# 1 - I need Python to read the .csv file
# 2 - I need Python to pick only the right columns and rows to read
# 3 - I need Python to sum the total value for all rows in one column, then do it for the other columns and store the total money spent of each column.
# 4 - I need Python to print the result and tells me in which column i spent the most during the month.

import csv
import os



# Using os lib to define the path for my test.csv file

current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, 'test.csv')

# opening and reading the file 

total = 0

with open(csv_path, encoding='utf-8') as csvfile_reader:
    reader = csv.DictReader(csvfile_reader)
    for row in reader:
        value = row['Ifood']
        if not value:
            continue
        clean_value = value.replace('R$', '').replace(',','.')
        total += float(clean_value)

print(total)
    




