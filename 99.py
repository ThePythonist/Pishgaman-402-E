lines = open("words.txt").read().replace("\n", " ")
open("1line.txt", "w").write(lines)
