with open("lingva.txt", "r", encoding = "utf-8") as f:
    line = f.readline()
    a = "Critically endangered"
    i = 0
    while line:
        line = line.split("    ")
        b = line[0]
        if a in b:
            i+=1
        line = f.readline()
    print("число таких строк равно", i)
