from pathlib import Path
import csv

import matplotlib.pyplot as plt
from datetime import datetime

# Get the path
path = Path('weather_data/sitka_weather_07-2021_simple.csv')
# Read the file and make a list of it.
lines = path.read_text().splitlines()

# Give a List of items and creating a reader object.
# reader object convert list items into individual list.
reader = csv.reader(lines)

# it return a next list from reader object.
header_row = next(reader)

# Extract high temperatures and date.
highs, dates = [], []

for row in reader:
    high = int(row[4])
    current_date = datetime.strptime(row[2], "%Y-%m-%d")

    highs.append(high)
    dates.append(current_date)

# Plot the high temperatures
plt.style.use(plt.style.available[16])
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', linewidth=3)

# Format plot
ax.set_title("Daily High Temperatures, July 2021", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
