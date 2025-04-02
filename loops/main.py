while True:
    n =int(input("How many times do you want the cat to meow?"))
    if n > 0:
        break
    else:
        print("Please enter a positive number.")

for _ in range(n):
    print("Meow!")