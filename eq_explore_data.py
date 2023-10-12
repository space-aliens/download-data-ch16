from pathlib import Path
import json

import plotly.express as px

path = Path("eq_data/eq_data_30_day_m1.geojson")
contents = path.read_text()
# JSON DATA -> PYTHON OBJECT
all_eq_data = json.loads(contents)

# Examine all earthquakes in dataset.
all_eq_dicts = all_eq_data['features']

# datasets
mags, lons, lats, eq_titles = [eq_dict['properties']['mag'] for eq_dict in all_eq_dicts], [eq_dict["geometry"]["coordinates"][0] for eq_dict in all_eq_dicts], [eq_dict["geometry"]["coordinates"][1] for eq_dict in all_eq_dicts], [eq_dict['properties']['title'] for eq_dict in all_eq_dicts]

# for eq_dict in all_eq_dicts:
#     mag = eq_dict['properties']['mag']
#     lon = eq_dict["geometry"]["coordinates"][0]
#     lat = eq_dict["geometry"]["coordinates"][1]
#     eq_title = eq_dict['properties']['title']

#     mags.append(mag)
#     lons.append(lon)
#     lats.append(lat)
#     eq_titles.append(eq_title)

title = all_eq_data["metadata"]["title"]
fig = px.scatter_geo(lat=lats, lon=lons, title=title, size=mags,
                     color=mags,
                     color_continuous_scale='mygbm',
                     labels={'color': 'Magnitude'},
                     projection='natural earth',
                     hover_name=eq_titles
                     )    
fig.show()




