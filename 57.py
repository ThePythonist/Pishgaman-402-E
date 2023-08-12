scores = {
    "riazi1": 14,
    "zaban": 20,
    "mabani computer": 19,
    "fizik1": 17,
    "andishe eslami": 8,
    "sakhteman dade": 16

}

for k, v in scores.items():
    if v >= 10:
        print(k, "Is Passed")
    else:
        print(k, "Is Failed")

moadel = sum(scores.values()) / len(scores)
print(moadel)
