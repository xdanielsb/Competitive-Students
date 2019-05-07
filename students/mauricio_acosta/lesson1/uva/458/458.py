from sys import stdin

while True:
    lines = stdin.readline().split()
    if not lines:
        break
    for line in lines:
        for letter in line:
            d = ord(letter)
            print("%c"%(d-7), end="")
            if not letter:
                exit()
        print()
