try:
    x = int(input("What's x ? "))
except ValueError:
    print("x is not an integer")

print(f"x is {x}")

# this gives a NameError at line 6 because passing a string the "string" and passing it to the int fuction makes no sense hence int function gives the NameError
# and the x is not equated to anything hence the not defined error.