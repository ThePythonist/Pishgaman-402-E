# number = 45675
number = int(input("Enter a 5 digit number : "))
if len(str(number)) == 5:
    for i in str(number):
        print(i)
else:
    print("Number must have 5 digits")
