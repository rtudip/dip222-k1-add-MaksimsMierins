r = 0
t = []
with open ("data.txt", "r") as file:
    next(file)
    for line in file: 
        row = line.rstrip().split(",")
        if row[8] == "Telecommunications" and row[5] == "Latvia" :
            print(row[8])