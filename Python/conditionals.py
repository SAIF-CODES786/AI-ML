age = int(input("Enter your age: ")) # without int it will be a string and comparison will not work correctly 

if age >= 18:
    print("You are an adult.")
    print("You can vote.")
else:
    print("You are a minor.")
    print("You cannot vote.")

color = input("Enter your favorite color: ")
if color == "red":
    print("Stop!")
elif color == "green":
    print("Go!")
elif color == "yellow":
    print("Caution!")
else:
    print("Invalid color.")



username = input("Enter your username: ") # without int it will be a string and comparison will not work correctly
password = input("Enter your password: ")

if(username == "admin" and password == "pass"):
    print("LOGIN Successfull")
elif (username != "admin"):
    print("wrong Username")
else: 
    print("wrong Password")


num = int(input("Enter a number: ")) # without int it will be a string and comparison will not work correctly
if (num%2 == 0):
    print("The number is even.")
else:
    print("The number is odd.") 





username = input("Enter your username: ") # without int it will be a string and comparison will not work correctly
password = input("Enter your password: ")

if(username == "admin" and password == "pass"):
    print("LOGIN Successfull")
else:
    if(username != "admin"):
        print("wrong Username")
    else:
        print("wrong Password")



# match 
color = input("enter color: ")

match color:
    case "Green":
        print("Go")
    case "Yellow":
        print("Look")
    case "Red":
        print("Stop")
    case _:
        print("wrong color!")      