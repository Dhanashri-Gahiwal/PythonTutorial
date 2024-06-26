# write json file
# import json module
import json

# create json data
jsonData = '[{"employee": [{"name":"Rahul", "age":28},{"name":"Dhanashri", "age":26},{"name":"Tejas", "age":24}],"company": [{"name": "Infosys", "location":"Pune"},{"name": "HummingByte", "location":"Nashik"},{"name": "Vishwa Technology", "location":"Nagpur"}]}]'

# open file
jsonFile = open("demo.json","w")

# write data
data = jsonFile.write(jsonData)

# store data
writeJson = json.dumps(data)

# close json file
jsonFile.close()
