from itertools import tee


def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    first, second = tee(iterable)
    next(second, None)
    return zip(first, second)
