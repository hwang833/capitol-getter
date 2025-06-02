import json


with open('state_capitals_normalized.json', 'r') as f:
    data = json.load(f)
lats = set(entry['latitude'] for entry in data if entry['latitude'] is not None)
lons = set(entry['longitude'] for entry in data if entry['longitude'] is not None)
print(f"Unique latitudes: {len(lats)}, Unique longitudes: {len(lons)}")