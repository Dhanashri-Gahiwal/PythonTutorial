# deserialize data(read data)
# step-1: import pickle module
import pickle

# step-2: open file in read mode to read data
file = open("data.txt","rb")

# step-3: read data using load() function
l = pickle.load(file)

print(l)