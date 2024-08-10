from math import inf
def divide(first, second):

    if int(second) == 0:
        return inf

    else:
        value = int(first) / int(second)
        return value


