# create dictionary
d = {
    'name' : 'Dhanshri',
    'age' : 26,
    'salary' : 25000,
    'address' : 'Nashik',
    'email' : 'dhanshri@gmail.com'
}
print(d)

# get()
print(d.get('name'))

# keys()
for k in d.keys():
    print(k)

# values()
for v in d.values():
    print(v)

# items()
for k,v in d.items():
    print(k,"=",v)

# update()
d.update(salary = 40000)
print(d)

# del
del d['email']
print(d)

# pop()
p = d.pop('address')
print(p)
print(d)

# clear()
d.clear()
print(d)

# #############################################################################################

# create nested dictionary
d2 = {
    'php' : {'duration' : '2 months', 'fees' : 2000},
    'python' : {'duration' : '4 months', 'fees' : 4000},
    'java' : {'duration' : '6 months', 'fees' : 8000}
}
print(d2)

# get() in nested dictionary
print(d2.get('php'))
print(d2.get('php').get('fees'))

# keys() in nested dictionary
for k in d2['php'].keys():
    print(k)

# values() in nested dictionary
for v in d2['php'].values():
    print(v)

# items() in nested dictionary
for k,v in d2['php'].items():
    print(k,"=",v)

# update() in nested dictionary 
d2['php'].update(fees = 4000)
print(d2)

d2.update(python = {'duration' : '6 months', 'fees' : 8000})
print(d2)

# pop() in nested dictionary
p1 = d2['python'].pop('fees')
print(p1)
print(d2)

p2 =d2.pop('python')
print(p2)
print(d2)

# del in nested dictionary
del d2['java']['fees']
print(d2)

del d2['java']
print(d2)