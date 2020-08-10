if __name__ == '__main__':
    N = int(input())
    students = list()
    for i in range(N):
        name = input()
        score = float(input())
        students.append([name, score])

    sec_highest = sorted(list(set([v for k, v in students])))[1]

    print('\n'.join([a for a, b in sorted(students) if b == sec_highest]))
