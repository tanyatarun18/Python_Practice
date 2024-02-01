print("hello world")

import keyword
print(keyword.kwlist)
#complex = it is a datatype which has real (4,3,etc) + imagianry (4j, 5j,etc(only in j)) values.

#List - list is used to store multiple data. list is mutable which means that the values can be changed.
list1 = ['Tanya','abc', 1, 4, 18]
list1[1] = 'Kunal'
print(list1)

#Tuple - Tuple is also used to store multiple data. It is not mutable( values cannot be changed)
tuple1 =('Hii',3,'Hello',45,6,98)
print(tuple1)

#Dictionary - dictionary is also used to stre multiple data. Its different from other two because the data member can be accessed through their
# keyword just like the real dictionary.
dict1 = {'Roll 1': 'Akanksha', 'Roll 2': 'Aryan', 'Roll 3': 'Akarsh', 'Roll 4': 'Sunaina'}
print(dict1)
print(dict1['Roll 3'])

#None - None is a datatype which is used when we don't want to assign the value to variable at that particular time.