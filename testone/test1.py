with open("lingva.txt", "r", encoding = "utf-8") as f:
    line = f.readline()
    while line:
        if len(line) > 35:
            print(line)
        line = f.readline()
