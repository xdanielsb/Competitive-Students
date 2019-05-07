#String
from sys import stdin

n=int(stdin.readline())
for _ in range(n):
    word=stdin.readline()
    if len(word)>11:
        centro=int(len(word[1::]))-2
        print('{0}{1}{2}'.format(word[0],centro,word[-2]))
    else:
        print(word, end='')
