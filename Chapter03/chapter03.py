#!/usr/bin/env python3
from typing import Callable
import math
# old usage: 定义class 可以不用继承object.(不推荐)
class Mersenne1:
    def __init__(self, algorithm: Callable[[int], int]) -> None:
        self.pow2 = algorithm
    def __call__(self, arg: int) -> int:
        return self.pow2(arg) - 1

def shifty(b: int) -> int:
    """ 
    >>> shifty(17) - 1
    131071
    """
    return 1 << b

def multy(b: int) -> int:
    """ 
    >>> multy(17) - 1 
    131071
    """
    if b == 0:
        return 1
    return 2*multy(b-1)

def faster(b: int) -> int:
    """ 
    this will use log_2^{b} step to calc the result, 
    Up functions will use b steps
    >>> faster(17) - 1
    131071
    """
    if b == 0:
        return 1
    if b%2 == 1:
        return 2*faster(b-1)
    t = faster(b//2)
    return t*t

def usage_Mersenne1():
    """ 
    >>> usage_Mersenne1()
    393213
    """
    m1s = Mersenne1(shifty)    
    m1m = Mersenne1(multy)
    m1f = Mersenne1(faster)
    a = m1s(17)
    b = m1m(17)
    c = m1f(17)
    return a+b+c


def pfactors_base(x):
    """
    >>> list(pfactors_base(36))
    [2, 2, 3, 3]
    """
    if x % 2 == 0:
        yield 2
        if x // 2 > 1:
            yield from pfactors_base(x//2)
        return
    for i in range(3, int(math.sqrt(x)+0.5)+1, 2):
        if x % i == 0:
            yield i
            if x // i > 1:
                yield from pfactors_base(x//i)
            return
    yield x


def pfactors_FP(x):
    """
    >>> list(pfactors_FP(36))
    [2, 2, 3, 3]
    """
    def factor_n(x, n):
        if n*n > x:
            yield x
            return
        if x % n == 0:
            yield n
            if x // n > 1:
                yield from factor_n(x//n, n)
        else:
            yield from factor_n(x, n+2)

    if x % 2 == 0:
        yield 2
        if x // 2 > 1:
            yield from pfactors_FP(x//2)
        return
    yield from factor_n(x, 3)
                












def test():
    import doctest
    doctest.testmod(verbose = True)
    


if __name__ == '__main__':
    test()
