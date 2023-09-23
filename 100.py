lines = open("words.txt").readlines()[::-1]
open("newwords.txt","w").writelines(lines)
