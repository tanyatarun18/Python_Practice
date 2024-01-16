# Python program to print even numbers in a list

list = [34,23,6,43,8,4,9,65]

print("Even numbers are: ", end = '')
for i in list:
    if (i%2 == 0):
        print(i,end = ' , ')
