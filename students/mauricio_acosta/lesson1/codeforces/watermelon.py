#Brute force, math
from sys import stdin

watermelokg= int(stdin.readline());

if watermelokg>=1 and watermelokg<=100:
    if watermelokg % 2 == 0:
        part=watermelokg/2
        if part>1:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
