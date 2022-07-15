import csv
with open('/Users/wt/Desktop/wuli.csv','r') as file:
    reader=csv.DictReader(file)
    column=[row['ptl_name'] for row in reader]
print(column)