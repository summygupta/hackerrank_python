def wrap(s, max_width):
    return "\n".join([s[i:i+max_width] for i in range(0, len(s), max_width)])
