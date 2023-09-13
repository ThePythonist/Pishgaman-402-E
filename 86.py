a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
print((lambda x, y: x if x > y else y)(a, b))
