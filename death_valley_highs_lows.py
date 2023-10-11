import matplotlib.pyplot as plt

import csv

from pathlib import Path

from datetime import datetime

path = Path("weather_data/death_valley_2021_simple.csv")

# List of Lines
contents = path.read_text().splitlines()

# a object containing individual List.
# Itretor
reader = csv.reader(contents)

# Return next item from itretor
header = next(reader)

# highs, lows, dates Datasets
highs, lows, dates = [], [], []

for row in reader:
    date = datetime.strptime(row[2], "%Y-%m-%d")

    try:
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f"Missing data for {date}")     

    highs.append(high)
    lows.append(low)
    dates.append(date)

# Plot
fig, ax = plt.subplots()
ax.plot(dates, highs, color="red", alpha= 0.5) 
ax.plot(dates, lows, color="blue") 
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

# Format plot
title = "Daily High and Low Temperatures, 2021\nDeath Valley, CA"
ax.set_title(title, fontsize=12)
ax.set_ylabel("Temperature", fontsize=12)
ax.set_xlabel("Date", fontsize=12)

# Prevent overlapping between dates - x
fig.autofmt_xdate()


plt.show()