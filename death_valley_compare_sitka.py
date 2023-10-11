from pathlib import Path
import csv

import matplotlib.pyplot as plt
from datetime import datetime

# Get the path
sitka = Path('weather_data/sitka_weather_2021_simple.csv')
death_valley = Path("weather_data/death_valley_2021_simple.csv")
# Read the file and make a list of it.
lines = sitka.read_text().splitlines()
lines2 = death_valley.read_text().splitlines()

# Give a List of items and creating a reader object.
# reader object convert list items into individual list.
sikta_reader = csv.reader(lines)
death_valley_reader = csv.reader(lines2)

# it return a next list from reader object.
sikta_header_row = next(sikta_reader)
death_valley_header_row = next(death_valley_reader)


# Extract high temperatures and date.
sikta_highs, sikta_lows, sikta_dates = [], [], []
death_valley_highs, death_valley_lows, death_valley_dates = [], [], []

for row in sikta_reader:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")

    try:
        high = int(row[4])
        low = int(row[5]) 
    except ValueError:
        continue
    else:    
        sikta_highs.append(high)
        sikta_lows.append(low)
        sikta_dates.append(current_date)


for row in death_valley_reader:
    date = datetime.strptime(row[2], "%Y-%m-%d")

    try:
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f"Missing data for {date}")     

    death_valley_highs.append(high)
    death_valley_lows.append(low)
    death_valley_dates.append(date)

# Plot the high temperatures
plt.style.use(plt.style.available[16])
fig, ax = plt.subplots()

# Highs
ax.plot(sikta_dates, sikta_highs, color='red',)
# Lows
ax.plot(sikta_dates, sikta_lows, color='blue')
# Fill color between highs and lows
ax.fill_between(sikta_dates, sikta_highs, sikta_lows, facecolor='blue', alpha=0.1)


# Highs
ax.plot(death_valley_dates, death_valley_highs, color='black',)
# Lows
ax.plot(death_valley_dates, death_valley_lows, color='green')
# Fill color between highs and lows
ax.fill_between(death_valley_dates, death_valley_highs, death_valley_lows, facecolor='pink', alpha=0.6)


# Format plot
ax.set_title("Daily High Temperatures 2021", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
