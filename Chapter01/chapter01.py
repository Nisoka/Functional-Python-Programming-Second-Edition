#!/usr/bin/python3

def sum_FP_base(seq):
    """ 

    >>> sum_FP_base(list(range(1, 5)))
    10

    """
    if seq == []:
        return 0
    return seq[0] + sum_FP_base(seq[1:])

def until(n, filter_func, v):
    """
    >>> list(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(10)))
    [0, 3, 5, 6, 9]
    >>> until(10, lambda x: x%3 == 0 or x%5 == 0, 0)
    [0, 3, 5, 6, 9]
    """
    if v == n:
        return []
    if filter_func(v):
        return [v] + until(n, filter_func, v + 1)
    else:
        return until(n, filter_func, v+1)

def folder(seq, op, init):
    """
    >>> folder(list(range(1, 5)), lambda x, y: x + y, 0)
    10
    """
    if seq == []:
        return init
    return op(seq[0], folder(seq[1:], op, init))

def sum_FP():
    """
    >>> sum_FP()
    23
    """
    multi_3_5 = lambda x: x % 3 ==0 or x % 5 == 0
    add = lambda x, y: x + y
    return folder(until(10, multi_3_5, 0), add, 0)

def sum_hybrid():
    """
    >>> sum_hybrid()
    23
    """
    print(sum(n for n in range(1, 10) if n % 3 == 0 or n % 5 == 0))



# next_ 进行一个接近操作, 让x 逐渐接近 n的sqrt n = x^2 => n对x的导数为 2x
def next_(n, x):
    return (x + n/x)/2

def sqrt_1():
    n = 2
    f = lambda x: next_(n, x)
    a0 = 1.0
    # round, 格式化数值为 n 位
    print([round(x, 4) for x in (a0, f(a0), f(f(a0)), f(f(f(a0))))])

# yield 关键字 会将函数 变为generator, 而不是普通函数,
# generator 会形成闭包, 具有 next 函数, 每次执行到 yield 进行return ;
def repeat(f, a):
    yield a

    # equivlent:
    # for v in repeat(f, f(a)):
    #     yield v
    yield from repeat(f, f(a))

# 返回一个函数, 从iterable 遍历到末尾, 找到两个邻接值 差值小于门限的值.
def within(epsilon, iterable):
    
    def head_tail(epsilon, a, iterable):
        b = next(iterable)
        if abs(a - b) < epsilon:
            return b
        return head_tail(epsilon, b, iterable)
    return head_tail(epsilon, next(iterable), iterable)


def sqrt_FP(a0, epsilon, n):
    """ 
    >>> sqrt_FP(1, 0.001, 2)
    1.4142
    """
    # 1 在一个list上逐个寻找n的平方根
    # 2 list由 逐渐靠近n的平方根的数构成
    # lambda x: next_(n, x) 生成从x处 开始更靠近n sqrt root的一个数
    # repeat 使用 lambda, 生成逐渐靠近n sqrt root的数list
    # within(head_tail) 逐渐比较该list, 找到最靠近的值
    print( round( within(epsilon, repeat(lambda x: next_(n, x), a0)), 4 ) )



def test():
    import doctest
    doctest.testmod(verbose = True)
    


if __name__ == '__main__':
    test()