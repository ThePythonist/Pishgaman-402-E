def checknumber(x):
    if type(x) in [int, float]:
        print("Okay continue")
        return "Number"
    else:
        print("Not okay")
        return "Not Number"


# print(checknumber(4.3))

#
# if checknumber(4.2) == "Number":
#     print("Yes")
# else:
#     print("No")

# -------------------------------------------

# def checknumber(x):
#     if x % 2 == 0:
#         print("Even")
#         # return "Even"
#     else:
#         print("Odd")
#         # return "Odd"
#
#
# # checknumber(7)
# # print(checknumber(14))
#
# # if checknumber(8) == "Even":
# #     print("Pasokh zoj ast")
#
numbers = [11, "SMT", 4, 2, 3, 5, 12, 16]
for i in numbers:
    checknumber(i)
