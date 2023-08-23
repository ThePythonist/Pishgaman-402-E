def filter(items):
    numbers = []
    for i in items:
        if type(i) in [int, float]:
            numbers.append(i)

    return numbers


items = [True, 12, 50, "Java", "Python", 1.5, 0.83, [], None]
print(filter(items))
