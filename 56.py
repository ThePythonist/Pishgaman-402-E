ages = {
    "parsia": 20, "armin": 21, "mohammad": 18,
    "helia": 30, "mohsen": 17, "sara": 26
}

oldest = max(ages.values())

for i in ages:
    if ages[i] == oldest:
        # print(i,ages[i])
        print(i)
