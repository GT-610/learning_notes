from pathlib import Path
import json

# Transfer JSON into Python objects
path=Path('eq_data/eq_data_1_day_m1.geojson')
contents=path.read_text()
all_eq_data=json.loads(contents)

# View all earthquakes
all_eq_features=all_eq_data['features']
# print(len(all_eq_features))

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

print(mags[:10])
print(titles[:10])
print(f"Location: {lons[:10]}, {lats[:10]}")