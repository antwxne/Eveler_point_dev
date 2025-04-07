import csv
import random

# Define the file name
file_name = '../resources/meters_info.csv'

# Define the column headers
headers = ['meter_id', 'conso', 'unit']

# Generate 1000000 rows of data
data = []
for i in range(0, 1000000):
    meter_id = i
    conso = random.randint(100, 1000)  # Random consumption value between 100 and 1000
    unit = 'W'
    data.append([meter_id, conso, unit])

# Write the data to a CSV file
with open(file_name, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(data)

print(f'CSV file "{file_name}" created successfully.')