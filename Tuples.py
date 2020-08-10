if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    input_list = list(integer_list)
    t = tuple(input_list)
    print(hash(t))
