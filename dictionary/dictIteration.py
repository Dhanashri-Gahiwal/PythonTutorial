# create dictionary
d = {
    'name' : 'Dhanshri',
    'age' : 26,
    'salary' : 25000
}
print(d)

# iterate dictionary
for k in d:
    print(k,"=",d[k])

# create nested dictionary
d2 = {
    'php' : {'duration' : '2 months', 'fees' : 2000},
    'python' : {'duration' : '4 months', 'fees' : 4000},
    'java' : {'duration' : '6 months', 'fees' : 8000}
}
print(d2)

# iterate nested dictionary
for k in d2:
    print(k,"=",d2[k])
    print(k,"=",d2[k]['duration'],d2[k]['fees'])
