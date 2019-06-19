from sys import stdin

case = int(stdin.readline())
count = 0
for _ in range(case):
    contests = stdin.readline().split()
    contests = list(map(int, contests))
    if sum(contests) >= 2:
        count+=1
print(count) 