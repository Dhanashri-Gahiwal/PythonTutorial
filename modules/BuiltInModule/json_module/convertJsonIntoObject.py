# convert json into python object
# import json module
import json

# create json data
jsonData = '{"course":"python","fees":12000,"duration":"2 months"}'
print("json:",jsonData,type(jsonData))

# convert json data into python object
to_object = json.loads(jsonData)
print(to_object,type(to_object))