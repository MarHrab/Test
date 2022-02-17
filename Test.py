# age = 20        #variable
# price = 19.95
# first_name = "Mar"
# in_online = True
# print(age, first_name)
#
# Hospital Task
#
# name = "John Smith"
# age = 20
# is_new = True
# print("Patient name is ", name)
# print("Patient age is ",  age)
# print("New patient check =", is_new)
#
# input things
# name = input("What is your name? ")
# print("Hello " + name)
#
#
# Types of variable
#
# birth_year = input("Enter you birth year: ")
# age = 2022 - int(birth_year)#int function(int(),float(),bool(), str())
# print(age)
#
# simple calculator
#
# first = float(input("First number: "))
# second = float(input("Second number: "))
# sum = first + second
# print("Sum is: " + str(sum))

# course = 'Python for Beginners'
# print(course.find('y'))
# print(course.replace('for' , '4'))
# print('Python' in course)

# arithmetic operation
# if use / float number, if // int number
# if 10 ** 3 = 1000
# x = 10
# x += 3 etc

#if statements

# temperature = 25
# if temperature > 30:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif temperature >20:
#     print("It's a nice day")
# elif temperature >10:
#     print("It's a bit cold")
# else:
#     print("It's cold")
# print("Done")



#func of factorial finding

x = int(input("Write a number to find factorial: " ))
def factorial(x):
    if x==1:
        return 1
    return factorial(x-1)*x
print("Factorial of your number is: " + str(factorial(x)))