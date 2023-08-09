number = int(input("Enter any number : "))
divisors = []

for i in range(1, number):
    if number % i == 0:
        divisors.append(i)

n = 0

for i in divisors:
    n += i

if number == n:
    print("Perfect number")
else:
    print("Not perfect")
