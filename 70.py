def numberstatus(x):
    if x % 2 == 0:
        print("Even")
    else:
        print("Odd")


def numbertype(x):
    if type(x) in [int, float]:
        numberstatus(x)
    else:
        print("Entry is not a number")


numbertype("Something")
