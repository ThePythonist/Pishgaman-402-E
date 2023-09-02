def f1(text):
    text = text.split()
    lengths = []

    for i in text:
        lengths.append(len(i))

    longest = max(lengths)

    for i in text:
        if len(i) == longest:
            print(i)


txt = "python is a good programming language"


# f1(txt)

def f2(text):
    text = text.split()
    text.sort(key=len)
    print(text[-1])


# f2(txt)

def f3(text):
    text = text.split()
    print(max(text, key=len))


f3(txt)
