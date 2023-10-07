from random import choice, sample


def generate1(digits):
    password = []
    for i in range(digits):
        x = choice(range(0, 9))
        password.append(str(x))

    password = "".join(password)
    return password


print(generate1(6))


def generate2(digits):
    password = [str(i) for i in sample(range(0, 9), digits)]
    password = "".join(password)
    return password


print(generate2(6))
