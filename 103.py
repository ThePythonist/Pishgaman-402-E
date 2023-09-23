lines = open("words.txt").read().split("\n")
items = []

for line in lines:
    if not line.isdigit():
        for char in line:
            if char.isdigit():
                items.append(line)
                break

print(items)
