def swap_case(s):
    t = []
    for i in s:
        if i.isupper():
            t.append(i.lower())
        else:
            t.append(i.upper())
    return (''.join(t))
