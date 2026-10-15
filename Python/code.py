print("hello world") 
# , && /n
 

# operators
# arithmetic operators
print(5 + 3)  # addition
print(5 - 3)  # subtraction
print(5 * 3)  # multiplication
print(5 / 3)  # division
print(5 % 3)  # modulus 
print(5 // 3)  # floor division
print(5 ** 3)  # exponentiation


# relational operators
print(5 > 3)  # greater than    
print(5 < 3)  # less than
print(5 == 3)  # equal to
print(5 != 3)  # not equal to
print(5 >= 3)  # greater than or equal to
print(5 <= 3)  # less than or equal to


# assignment operators
x = 5
print(x)  # prints 5
x += 3
print(x)  # prints 8
x -= 3
print(x)  # prints 5
x *= 3
print(x)  # prints 15
x /= 3
print(x)  # prints 5.0
x %= 3
print(x)  # prints 2.0
x //= 3
print(x)  # prints 0


# logical operators
print(True and False)  # prints False
print(True or False)  # prints True
print(not True)  # prints False
print(not False)  # prints True


# operators precedence - ()  **  *,/,%,//  +,-  ==,!=,>,<,>=,<=  not  and   or
print(5 + 3 * 2)  # prints 11
print((5 + 3) * 2)  # prints 16
print(5 ** 3)  # prints 125



# TYPE CONVERSION
# implicit type conversion
x = 5
print(x)  # prints 5
x = float(x)
print(x)  # prints 5.0


# TYPE CASTING
# explicit type conversion
x = 5.5
print(x)  # prints 5.5
x = int(x)
print(x)  # prints 5


# INPUT FUNCTION
name = input("Enter your name: ")
print("Hello, " + name + "!")  # prints Hello, <name>!

A = int(input("Enter a number: ")) 
# // without int() it will be a string
B = int(input("Enter another number: "))
print("The sum of", A, "and", B, "is", A + B)  # prints the sum of A and B

a = float(input("Enter a number: "))
b = float(input("Enter another number: "))
print("the avg of", a, "and", b, "is", (a + b) / 2)  # prints the average of a and b