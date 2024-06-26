# serialize data(store data)
# step-1: import pickle module
import pickle

# step-2: create list
l = [12,23,34,45,56]

# step-3: open file in write mode
file = open("data.txt","wb")

# step-4: store the data using dump() function
pickle.dump(l,file)

# step-5: close file
file.close()