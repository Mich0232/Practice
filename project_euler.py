""" https://projecteuler.net/archives - solutions
"""
import math


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
        ID: 2
        Returns sum of all even fibonacci numbers
    """
    fib, sum = fibonacci(), 0
    number = next(fib)
    while number < cap:
        if number % 2 == 0:
            sum += number
        number = next(fib)
    return sum


def prime_factors(number):
    """
        ID: 3
        Returns list of prime factors of given number
    """
    if not isinstance(number, int) or number < 2:
        raise ValueError("Number needs to be an integer larger then 1")

    limit = int(math.sqrt(number))
    factors = []
    while number != 1:
        for x in range(2, limit):
            if number % x == 0:
                number = number / x
                factors.append(x)
                break
        else:
            factors.append(int(number))
            break
    return factors
# print(max(prime_factors(600851475143))) # largest prime factor
