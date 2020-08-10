import itertools


def count_substring(s, sb):
    t = list(s)
    l = len(sb)
    count = 0
    for i in range(len(t)):
        if ''.join(t[i:i+l]) == sb:
            count = count+1
    return count
