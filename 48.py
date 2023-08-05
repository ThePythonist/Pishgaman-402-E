n = int(input("Enter any number : "))
divs = []

for i in range(1, n + 1):
    if n % i == 0:
        divs.append(i)

print(divs)
if len(divs) == 2:
    print("Prime")
else:
    print("Composite")
