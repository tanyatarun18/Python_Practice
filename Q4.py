# Given a list, write a Python program to swap first and last element of the list.

def swap(List):
    n = len(List)

    x = List[n-1]
    List[n-1]=List[0]
    List[0]=x
    return List

List = [2,4,13,54,45,23,54,65,8]
result = swap(List)
print(result)