import datetime


def f1():
    now = str(datetime.datetime.now()).split()
    time = now[1]
    print(time)
    print(time[0:5])


def f2():
    now = datetime.datetime.now()
    print(now.hour, end=":")
    print(now.minute)


f2()
