lines = open("words.txt").readlines()
inglist = []
for i in lines:
    # if i[-4:-1] == "ing":
    if "ing" in i[-4:]:
        inglist.append()

print(inglist)
