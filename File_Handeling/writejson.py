import json
person = {"name": "bbb",
          "language": "hindi"}

with open("file.json", "w") as f:
    json.dump(person,f)