# Creating a dictionary
hello = {'Name':'Tanya', 'Title':'Tarun', 'Course':'Btech', 'Age':19}
print(hello)

'''#Accessing values through keys
print(hello['Title'])

# Another method to access value
print(hello.get('Age')

# Modifying the value
hello['Age'] = 20
hello['Course'] = 'Btech (Cse)'
print(hello['Age'])
print(hello.get('Course'))

# Adding new key/value to the dictionary
hello['Roll'] = '19'
print(hello)

# Removing keys/values through two ways
# 1. delete
del hello['Age']
print(hello)

# 2. Pop
hello.pop('Roll')
print(hello)

# Checking for existence of any key
if 'Name' in hello:
 print("Hii")

# Converting the keys/values into lists separately
print(list(hello.keys()))
print(list(hello.values()))
# We can convert the keys/values in list and print in a single list too.
a = list(hello.keys())
b = list(hello.values())
print(a+b)
a.extend(b)
#extend is a function which extends the values of 2nd variable to 1st making it combined in a single line.
print(a)

# Clearing the dictionary
hello.clear()
print(hello)'''

# Merging dictionaries using update function
hello1 = {'course code': 'P132', 'Year':'2nd', 'Semester':'4th'}
hello.update(hello1)
print(hello)