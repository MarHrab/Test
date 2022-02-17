#func of factorial finding

x = int(input("Write a number to find factorial: " ))
def factorial(x):
    if x == 1: #check to out
        return 1
    return factorial(x-1)*x # factorial calculating
print("Factorial of your number is: " + str(factorial(x)))