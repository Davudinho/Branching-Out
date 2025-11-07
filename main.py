import json

with open("users.json") as f:
    data = json.load(f)
    print(data)
