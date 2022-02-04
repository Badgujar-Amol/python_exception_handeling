# application without exception handling
# print(10/0)

# using exception handling
try:
    print(10 / 0)
except:
    print("division by zero")

#
try:
    print(10 / 0)
except:
    print('division by zero')
print("hello")

#
try:
    print(10 / 0)
except NameError:
    print("Invalid error")
except ZeroDivisionError:
    print("division by zero")
print("Hello")


# else keyword in exception
try:
    print(i+j)
except NameError:
    print("variable not defined")
else:
    print("code is running well")

# finally keyword
try:
    print(i+j)
except NameError:
    print("variable not defined")
finally:
    print("This line is always executed")

# throw an exception
x = int(input("enter number"))
if x<10:
    raise Exception("value must be above 10")