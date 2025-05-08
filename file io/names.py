name = input("Enter a name: ")


file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()