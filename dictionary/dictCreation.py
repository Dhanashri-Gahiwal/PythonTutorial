# create dictionary
d = {
    'name' : 'Dhanshri',
    'age' : 26,
    'salary' : 25000
}
print(d)

# get dictionary value
print(d['name'])

# add element in existing dictionary
d['address'] = 'Nashik'
print(d)

# update element in existing dictionary
d['salary'] = 40000
print(d)

# create dictionary with dict() function
d1 = dict(name = 'Dhanshri', age = 26, salary = 25000)
print(d1)

# create nested dictionary
d2 = {
    'php' : {'duration' : '2 months', 'fees' : 2000},
    'python' : {'duration' : '4 months', 'fees' : 4000},
    'java' : {'duration' : '6 months', 'fees' : 8000}
}
print(d2)

# get nested dictionary value
print(d2['java']['fees'])

# add element in existing nested dictionary
d2['.net'] = {'duration' : '4 months', 'fees' : 8000}
print(d2)

# update element in existing nested dictionary
d2['.net'] = {'fees' : 10000}
print(d2)
d2['.net']['duration'] = '6 months'
print(d2)

# create nested dictionary with dict() function
d3 = dict(
    php = dict(duration = '2 months', fees = 2000),
    python = dict(duration = '4 months', fees = 4000),
    java = dict(duration = '6 months', fees = 8000),
    )
print(d3)