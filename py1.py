t = input("text: ") 

with open ("data.txt", "r") as file:
    next(file)
    for line in file: 
        row = line.rstrip().split(",")
        for t in row[5]:
            if row[6] == str(1970):
                print(row[6])
                break