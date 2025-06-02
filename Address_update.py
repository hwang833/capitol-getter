from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable
import json
from time import sleep

with open('state_capitals.json', 'r') as f:
    capitals = json.load(f)

geolocator = Nominatim(user_agent="state_capital_locator")

for entry in capitals:
    address = entry['address']
    try:
        location = geolocator.geocode(address, timeout=10)
        if location:
            entry['latitude'] = location.latitude
            entry['longitude'] = location.longitude
        else:
            entry['latitude'] = None
            entry['longitude'] = None
    except (GeocoderTimedOut, GeocoderUnavailable) as e:
        print(f"Error for {address}: {e}")
        entry['latitude'] = None
        entry['longitude'] = None
    sleep(2)  # 2 seconds between requests

with open('state_capitals_with_latlon.json', 'w') as f:
    json.dump(capitals, f, indent=2)