if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    s = sorted(arr, reverse=True)
    highest = s[0]
    for x in s:
        if x != highest:
            print(x)
            break

