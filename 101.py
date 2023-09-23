lines = open("words.txt").readlines()
rev = []
for line in lines:
    rev.append(line[::-1])

open("newwords.txt", "w").writelines(rev)
