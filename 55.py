info = {
    "name": "pishgaman",
    "city": "tehran",
    "type": "IT",
    "teacher": "sadeghi",
    "course": "python",
    "members": 8
}

key = input("Search any key : ")

# if key in info:
#     print("Found :", info[key])
# else:
#     print("Key not found")

try:
    print(info[key])
except KeyError:
    print("Key not found")
