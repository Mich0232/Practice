""" https://projecteuler.net/archives - solutions
"""
import math
from timeit import default_timer as timer

from algorithms import fibonacci_gen, prime_numbers_gen, pythagorean_triplet_gen, lcm


def sum_of_multiplies(cap):
    """
        ID: 1
        Returns sum of all numbers that are multiplies of 3 and 5
    """
    l = [d for d in range(cap)]
    func = lambda x: True if x % 3 == 0 or x % 5 == 0 else False
    return sum(filter(func, l))


def even_fibonacci(cap):
    """
        ID: 2
        Returns sum of all even fibonacci numbers
    """
    fib, sum_ = fibonacci_gen(), 0
    number = next(fib)
    while number < cap:
        if number % 2 == 0:
            sum_ += number
        number = next(fib)
    return sum_


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
        for x in range(2, limit + 1):
            if number % x == 0:
                number = number / x
                factors.append(x)
                break
        else:
            factors.append(int(number))
            break
    return factors


def palindrome_numbers():
    """
        ID: 4
        Returns list of palindrome numbers
    """
    palindromes = []
    for x in range(100, 999):
        for y in range(100, 999):
            number = x * y
            if str(number) == str(number)[::-1]:
                palindromes.append(number)
    return palindromes


def smallest_multiple():
    """
        ID: 5
        Returns number that is evenly divisible by all of the numbers from 1 to 20
    """
    l = [d for d in range(2, 20)]
    while len(l) > 1:
        number = lcm(l[0], l[1])
        l[1] = number
        del l[0]
    return l[0]


def square_diff():
    """ ID: 6
        Returns the difference between sum of squares and square of sum
    """
    a, b = 0, 0
    for x in range(101):
        a += x
        b += pow(x, 2)
    return pow(a, 2) - b


def prime_numbers(n):
    """ ID: 7
        Returns 'n'th prime number """
    if n == 1:
        return 2
    if n == 2:
        return 3
    gen = prime_numbers_gen()
    for _ in range(n-3):
        next(gen)
    return next(gen)


def pattern_matching():
    """ ID: 8
        Returns greatest product of multiplying 'n' adjacent digits """
    # TODO: solve that


def pythagorean_triplet():
    """ ID: 9
        Returns pythagorean triplet for which a+b+c = 1000"""
    # TODO: Better search algorithm
    gen = pythagorean_triplet_gen()
    factors = next(gen)
    while sum(factors) < 1000:
        factors = next(gen)
        print(factors, sum(factors))


def sum_of_primes():
    """ ID: 10
        Return sum of all primes below 2 millions"""
    gen = prime_numbers_gen()
    sum_ = 5
    prime = next(gen)
    while prime < 2000000:
        sum_ += prime
        prime = next(gen)
    return sum_


def get_fullname():
    return "Mark Zuckerberg"


def get_current_date():
    import datetime
    return datetime.datetime.now()


if __name__ == '__main__':
    pass
