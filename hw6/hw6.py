with open("text.txt", "w", encoding="utf-8") as f:
    print("Начинайте ввод латинских слов ")
    w=input()
    if w=="":
        print("пустая строка")
    else:
        while w!="":
            if w.endswith("tur"):
                f.write(a)
                f.write("\n")
            w=input()
