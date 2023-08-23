# def primestatus(n):
#     divs = [i for i in range(1, n + 1) if n % i == 0]
#     print("Prime") if len(divs) == 2 else print("Composite")
#
#
# n = int(input("Enter any number : "))
# primestatus(n)

def primestatus(n):
    divs = [i for i in range(1, n + 1) if n % i == 0]
    return "Prime" if len(divs) == 2 else "Composite"


n = int(input("Enter any number : "))
print(primestatus(n))
