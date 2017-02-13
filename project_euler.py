""" https://projecteuler.net/archives - solutions
"""
def sum_of_multiplies(cap):
    """
        ID: 1
        Returns sum of all numbers that are multiplies of 3 and 5
    """
    l = [d for d in range(cap)]
    func = lambda x: True if x % 3 == 0 or x % 5 == 0 else False
    return sum(filter(func, l))

def fibonacci():
    """Fibonacci numbers generator"""
    x, y = 1, 2
    while 1:
        yield x
        x, y = y, x+y

def even_fibonacci(cap):
    """
        ID: 1
        Returns sum of all even fibonacci numbers
    """
    fib, sum = fibonacci(), 0
    num = next(fib)
    while num < cap:
        if num % 2 == 0:
            sum += num
        num = next(fib)
    return sum
print(even_fibonacci(4000000))

