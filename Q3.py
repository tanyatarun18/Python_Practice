#Find the Factorial of a Number Using Recursive approach
def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
            return n * factorial(n-1)

n = int(input("Enter your number: "))
fact = factorial(n)
print(fact)