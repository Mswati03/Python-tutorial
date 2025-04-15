def main():
    x = get_int("What's x ? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("x is not an integer")

    # this gives a NameError at line 6 because passing a string the "string" and passing it to the int fuction makes no sense hence int function gives the NameError
    # and the x is not equated to anything hence the not defined error.


main()
