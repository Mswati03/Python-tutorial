with open("names.csv","r") as file:
    for line in file:
        row = line.strip().split(",")
        print(row[0],"is in ", row[1])
      