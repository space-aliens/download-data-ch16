from pathlib import Path
import csv

# Get the path
path = Path('weather_data/sitka_weather_07-2021_simple.csv')
# Read the file and make a list of it.
lines = path.read_text().splitlines()

# Give a List of items and creating a reader object.
# reader object convert list items into individual list.
reader = csv.reader(lines)

# it return a next list from reader object.
header_row = next(reader)

# enumerate() return index of item and item value.
for index, column_header in enumerate(header_row):
    print(index, column_header)
