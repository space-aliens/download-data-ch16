from pathlib import Path
import csv

import matplotlib.pyplot as plt

# Get the path
path = Path('weather_data/sitka_weather_07-2021_simple.csv')
# Read the file and make a list of it.
lines = path.read_text().splitlines()

# Give a List of items and creating a reader object.
# reader object convert list items into individual list.
reader = csv.reader(lines)

# it return a next list from reader object.
header_row = next(reader)

# Extract high temperatures.
highs = []
for row in reader:
    high = int(row[4])
    highs.append(high)

# Plot the high temperatures
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(9, 8))
ax.plot(highs, color='red', linewidth=3)

# Format plot
ax.set_title("Daily High Temperatures, July 2021", fontsize=24)
ax.set_aspect('equal')
ax.set_xlabel("", fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
