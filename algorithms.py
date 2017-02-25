""" Algorithms for solving project euler problems """

import math


def fibonacci_gen():
    """Fibonacci numbers generator"""
    x, y = 1, 2
    while 1:
        yield x
        x, y = y, x+y


def lcm(a, b):
    """ Return lowest common multiple of a and b """
    return a * b // math.gcd(a, b)


def prime_numbers_gen():
    """ Prime numbers generator (larger then 5)"""
    number = 5
    while 1:
        limit = int(math.sqrt(number))
        for x in range(3, limit + 1):
            if number % x == 0:
                break
        else:
            yield number
        number += 2


def pythagorean_triplet_gen():
    """ Generates pythagorean_triplets """
    n, m = 1, 2
    while 1:
        h = n + m
        g = m + h
        a = (2*m*h)
        b = (n*g)
        c = (2*m*h) + pow(n, 2)
        yield [a, b, c]
        n += 1
        m += 1


if __name__ == '__main__':
    pass
