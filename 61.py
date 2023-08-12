word = "engineer"
d = {}

for i in range(len(word)):
    d.setdefault(i, word[i])

print(d)
