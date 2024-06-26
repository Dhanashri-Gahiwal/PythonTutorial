# convert python object into json
# import json module
import json

# create python object (create dictionary)
d = {"course":"python","fees":12000,"duration":"4 months"}
print(d,type(d))

# convert into json using dumps() function
to_json = json.dumps(d)

print(to_json,type(to_json))