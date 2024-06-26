# read json file
# import json module
import json

# open json file
jsonFile = open("demo.json","r")

# read json file
readJson = jsonFile.read()

# convert into python object
data = json.loads(readJson)

print(data, type(data))

# iterate list
for i in data:
    print(i)
    l = i['employee']
    print(l)

for j in l:
    print(j)
    print(j['name'],j['age'])
