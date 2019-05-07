def main():
    variable=int(input())
    for _ in range(variable):
        numbers = input().split()
        numbers = [int(x) for x in numbers]
        if numbers[0] < numbers[1]:
            print ("<")
        elif numbers[0] > numbers[1]:
            print(">")
        else:
            print ("=")

if __name__ == '__main__':
    main()
