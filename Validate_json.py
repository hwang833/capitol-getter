import json

with open("state_capitals.json", "r") as f:
    data = json.load(f)
print("original state capital JSON is valid. Number of entries:", len(data))

with open('state_capitals_normalized.json', 'r') as f:
    data_2 = json.load(f)
print("JSON with longitude and latitude is valid. Number of entries:", len(data_2))