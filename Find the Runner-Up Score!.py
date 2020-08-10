if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    first = second = -2147483648
    if n < 2:
        print("invalid array")
    for i in range(n):
        if (arr[i] > first):
            second = first
            first = arr[i]
        elif (arr[i] > second and arr[i] != first):
            second = arr[i]
    if second == -2147483648:
        print("no runner up")
    else:
        print(second)
