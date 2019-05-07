from sys import stdin
def main():
    case=int(stdin.readline())
    if case>=20:
        exit()
    for i in range(case):
        salario=[int(x) for x in stdin.readline().split()]
        for j in salario:
            if not(1000<=j<=10000):
                continue
        salario.sort()
        print("Case {}: {}".format(i+1,salario[1]))
if __name__ == '__main__':
    main()
