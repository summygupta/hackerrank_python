def command(lst, instruction):
    if instruction[0] == 'insert':
        lst.insert(int(instruction[1]), int(instruction[2]))
    elif instruction[0] == 'print':
        print(lst)
    elif instruction[0] == 'remove':
        lst.remove(int(instruction[1]))
    elif instruction[0] == 'append':
        lst.append(int(instruction[1]))
    elif instruction[0] == 'sort':
        lst.sort()
    elif instruction[0] == 'pop':
        lst.pop()
    elif instruction[0] == 'reverse':
        lst.reverse()


if __name__ == '__main__':
    N = int(input())
    lst = []

    for i in range(0, N):
        tokens = [str(i) for i in input().strip().split()]
        command(lst, tokens)
