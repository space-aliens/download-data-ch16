from pathlib import Path
import csv

import matplotlib.pyplot as plt
from datetime import datetime

# Get the path
path = Path('weather_data/sitka_weather_2021_simple.csv')
# Read the file and make a list of it.
lines = path.read_text().splitlines()

# Give a List of items and creating a reader object.
# reader object convert list items into individual list.
reader = csv.reader(lines)

TMAX = 0
TMIN = 0
station_name = ''

# it return a next list from reader object.
header_row = next(reader)

for index, column_value in  enumerate(header_row):
    if column_value == 'TMAX':
        TMAX += index
    elif column_value == 'TMIN':
        TMIN += index
    elif column_value == 'NAME':
        station_name = column_value



# Extract high temperatures and date.
highs, lows, dates = [], [], []

for row in reader:
    high = int(row[4])
    low = int(row[5]) 
    current_date = datetime.strptime(row[2], "%Y-%m-%d")

    highs.append(high)
    lows.append(low)
    dates.append(current_date)

# Plot the high temperatures
plt.style.use(plt.style.available[16])
fig, ax = plt.subplots()

# Highs
ax.plot(dates, highs, color='red',)
# Lows
ax.plot(dates, lows, color='blue')
# Fill color between highs and lows
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)


# Format plot
ax.set_title(f"Daily High Temperatures of {station_name}", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
