def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


x = int(input("Enter number : "))
if x > 0:
    print(factorial(x))
elif x == 0:
    print("Factorial of zero is one")
else:
    print("Factorial doesnt exist")
