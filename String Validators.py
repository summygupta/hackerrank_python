if __name__ == '__main__':
    s = input()
    t = [i for i in s if i.isalnum()]
    if len(t) > 0:
        print("True")
    else:
        print("False")
    t = [i for i in s if i.isalpha()]
    if len(t) > 0:
        print("True")
    else:
        print("False")
    t = [i for i in s if i.isdigit()]
    if len(t) > 0:
        print("True")
    else:
        print("False")

    t = [i for i in s if i.islower()]
    if len(t) > 0:
        print("True")
    else:
        print("False")

    t = [i for i in s if i.isupper()]
    if len(t) > 0:
        print("True")
    else:
        print("False")
