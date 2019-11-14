from typing import List, Callable


def compose(*fns: List[Callable]) -> Callable:
    if len(fns) == 1:
        return fns[0]
    else:
        def composed(*args, **kwargs):
            return fns[0](compose(*fns[1:])(*args, **kwargs))
        return composed


if __name__ == '__main__':

    def get_f(n):
        return lambda x: x + n

    compose(print, get_f(1), get_f(2))(0)  # => 3
