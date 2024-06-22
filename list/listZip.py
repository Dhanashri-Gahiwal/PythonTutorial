l1 = [1,2,3,4]
l2 = [5,6,7,8]
l3 = [9,10,11,12]

# iterate multiple list using zip
for m,n,o in zip(l1,l2,l3):
    print(m,n,o)

# iterate multiple list using range
l = len(l1)
for m in range(l):
    print(l1[m],l2[m],l3[m])

# Note: the length of each and every list must be same