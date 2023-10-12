import csv

from pathlib import Path

import plotly.express as px

path = Path('world_fire_data/world_fires_1_day.csv')
contents = path.read_text().splitlines()

# Iteratable object
# Containing Mulitple individual List.
reader = csv.reader(contents)

# First row or List in reader object.
header_row = next(reader)

print(header_row)
lats, lons, brightness = [], [], []

for row in reader:
    try:
        lat = float(row[0]) 
        lon = float(row[1])
        bright = float(row[2])
    except ValueError:
        print("Data is not available.")
    else:
       
        lats.append(lat)
        lons.append(lon)
        brightness.append(bright)

print(lats[:10])
print(lons[:10])
print(brightness[:10])





# Ploting Dataset on World Map
title = "World Fires"
labels = {'x': "Lag", 'y':"Long", 'color':"Brightness"}

fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    title=title,
    size=brightness,
    color=brightness,
    # color_continuous_scale='red',
    labels=labels

)
fig.show()

