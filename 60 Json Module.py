# ------------------------ Python JSON ----------- #
"""
JSON is a syntax for storing and exchanging data.

JSON is text, written with JavaScript object notation.
"""
import json

data = '{"var1":"sherry", "var2":56}'

parsed = json.loads(data)

print(parsed['var1'])

data2 = {
    "Sherry": "Programmer",
    "Sherry_courses": ["Python", "Web", "PHP"],
    "Sherry_age": 16,
    "Sherry_isbad" : False
}

json_comp = json.dumps(data2)  # now this data is json compatible
print(json_comp)


# ------------- Tasks ------------- #
# Task 1 - json.load()
details = { "emp": [
    {"Sherry": "Programmer"},
    {"Hamza": "Engineer"},
    {"Zulqarnain": "Doctor"}
]}

# Task 2 - sort_key in json.dump

# Use the sort_keys parameter to specify if the result should be sorted or not:

for_sort = json.dumps(data2, sort_keys=True)
print(for_sort)