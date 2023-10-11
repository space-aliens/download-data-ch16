import csv

from pathlib import Path

from datetime import datetime

import matplotlib.pyplot as plt



# Path
path = Path("weather_data/sitka_weather_2021_full.csv")

contents = path.read_text().splitlines()

# Iterator object : itr->self  and next-> index+=1 
reader = csv.reader(contents)

header = next(reader)

# Date sets
dates, rainfalls = [], []

for row in reader:
    date = datetime.strptime(row[2], "%Y-%m-%d")
    try:
        rainfall = int(row[4])
    except ValueError:
        print(f"Missing Rainfall data at {date}")    
    else:
        rainfalls.append(rainfall)
        dates.append(date)

# Data Visualization
fig, ax = plt.subplots()

ax.plot(dates, rainfalls, color="green")
fig.autofmt_xdate()

plt.show()
