data = [True, True, 25, "Tokyo", 3.8, 10, 5.5, [], "Paris"]
# numbers = list(filter(lambda x: x if type(x) in [int, float] else None, data))
# print(numbers)
numbers = filter(lambda x: type(x) in [int, float], [2, 12.5, True])
print(list(numbers))
