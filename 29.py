a = 0
b = 1

for i in range(100):
    print(a)
    # c = a+b
    # a = b
    # b = c
    a, b = b, a + b
