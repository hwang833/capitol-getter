import json
import requests
from time import sleep

# Set your API key here
GOOGLE_API_KEY = 'AIzaSyB_eRt50hmLwWTYfTWsH1lO11gX0XIlM7Q'

def google_geocode(address, api_key):
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {"address": address, "key": api_key}
    resp = requests.get(url, params=params)
    data = resp.json()
    if data["status"] == "OK":
        result = data["results"][0]
        components = result["address_components"]
        lat = result["geometry"]["location"]["lat"]
        lng = result["geometry"]["location"]["lng"]

        # Initialize fields
        street = city = state = zipCode = None

        for c in components:
            if "street_number" in c["types"]:
                street_number = c["long_name"]
            if "route" in c["types"]:
                route = c["long_name"]
            if "locality" in c["types"]:  # City
                city = c["long_name"]
            if "administrative_area_level_1" in c["types"]:  # State
                state = c["short_name"]
            if "postal_code" in c["types"]:
                zipCode = c["long_name"]

        street = f"{street_number} {route}" if 'street_number' in locals() and 'route' in locals() else None

        return {
            "street": street,
            "city": city,
            "state": state,
            "zipCode": zipCode,
            "latitude": lat,
            "longitude": lng
        }
    else:
        return None

# Load your original data
with open('state_capitals.json', 'r') as f:
    capitals = json.load(f)

output = []

for entry in capitals:
    state = entry["state"]
    capital = entry["capital"]
    original_address = entry["address"]
    print(f"Processing: {capital}, {state} -- {original_address}")

    result = google_geocode(original_address, GOOGLE_API_KEY)
    sleep(0.2)

    if result:
        out_entry = {
            "state": state,
            "capital": capital,
            "address": {
                "street": result["street"],
                "city": result["city"],
                "state": result["state"],
                "zipCode": result["zipCode"]
            },
            "latitude": result["latitude"],
            "longitude": result["longitude"]
        }
    else:
        out_entry = {
            "state": state,
            "capital": capital,
            "address": {
                "street": None,
                "city": None,
                "state": None,
                "zipCode": None
            },
            "latitude": None,
            "longitude": None
        }
    output.append(out_entry)

with open('state_capitals_structured.json', 'w') as f:
    json.dump(output, f, indent=2)

print("Done! Structured address JSON created.")