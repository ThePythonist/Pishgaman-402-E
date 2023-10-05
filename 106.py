import datetime


def show_age1(birth):
    now = str(datetime.datetime.now()).split("-")
    thisyear = now[0]
    age = int(thisyear) - birth
    print(age)


# show_age1(1990)


def show_age2(birth):
    thisyear = int(datetime.datetime.now().year)
    age = thisyear - birth
    print(age)


show_age2(2009)
