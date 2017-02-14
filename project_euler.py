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


def fibonacci_gen():
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


def lcm(a, b):
    """
        Return lowest common multiple of a and b
    """
    return a *b // math.gcd(a, b)


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


def prime_numbers_gen():
    """ Prime numbers generator"""
    x = 2
    while 1:
        if prime_factors(x)[0] == x:
            yield x
        x += 1


def prime_numbers(n):
    """ ID: 7
        Returns 'n'th prime number """
    gen = prime_numbers_gen()
    for _ in range(n-1):
        next(gen)
    return next(gen)
