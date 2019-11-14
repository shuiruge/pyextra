from functools import reduce
from typing import List, Callable


def identity(x):
    return x


def compose(*fns: List[Callable]) -> Callable:

    def compose2(f, g):
        return lambda x: f(g(x))

    return reduce(compose2, fns, identity)


if __name__ == '__main__':

    def get_f(n):
        return lambda x: x + n

    compose(print, get_f(1), get_f(2))(0)  # => 3
