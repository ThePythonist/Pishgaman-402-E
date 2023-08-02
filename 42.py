pythons = ["ali", "hadi", "kourosh", "parisa"]
javas = ["parisa", "armina", "ali", "shahin"]
common = []

# for i in pythons:
#     if i in javas:
#         common.append(i)
#

for i in pythons:  # Martabe ejrayi = i * j
    for j in javas:
        if i == j:
            common.append(i)
print(common)
