# Python has a built-in package called json, which can be used to work with JSON data.

import json

# Parsing json to python or python to json.


# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])




# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)




#  https://www.w3schools.com/python/python_json.asp












