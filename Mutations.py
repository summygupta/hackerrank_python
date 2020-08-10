def mutate_string(s, position, character):
    temp = list(s)
    temp[position] = character

    return (''.join(temp))
