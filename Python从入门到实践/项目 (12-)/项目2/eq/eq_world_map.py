from pathlib import Path
import json
import plotly.express as px
import pandas as pd

# Transfer JSON into Python objects
path=Path('eq_data/eq_data_1_day_m1.geojson')
contents=path.read_text()
all_eq_data=json.loads(contents)

# Extract ll earthquakes
all_eq_features=all_eq_data['features']

# Extract
mags,titles,lons,lats=[],[],[],[]
for eq_feature in all_eq_features:
    # Mag
    mag=eq_feature['properties']['mag']
    mags.append(mag)

    # Title
    title=eq_feature['properties']['title']
    titles.append(title)

    # Geometry locations
    lon=eq_feature['geometry']['coordinates'][0]
    lat=eq_feature['geometry']['coordinates'][1]
    lons.append(lon)
    lats.append(lat)

# Zip all datas
data=pd.DataFrame(
    data=zip(lons,lats,title,mags),columns=["Lons","Lats","Title","Mags"]
)
data.head()

# Set the parameters
fig=px.scatter(
    data,
    x="Lons",
    y="Lats",
    range_x=[-180,180],
    range_y=[-90,90],
    size="Mags",
    size_max=10,
    title="Global Earthquake Scatter Map"
)

# Draw
fig.show()