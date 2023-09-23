def extract():
    lines = open("words.txt").read().split("\n")

    for i in lines:
        if i.isdigit():
            print(i)


extract()
