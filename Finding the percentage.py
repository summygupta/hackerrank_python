if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sum = 0
    for k, v in student_marks.items():
        if k == query_name:
            for i in v:
                sum = sum+i
            avg = round(sum/3, 2)
            print("%.2f" % avg)
