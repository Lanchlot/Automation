import json
json_data = {"name": "Zophie", "isCat": True, "miceCaught": 0, "felineIQ": None}
python_data = json.load(json_data)
print(python_data)
