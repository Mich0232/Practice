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


def pattern_matching(n):
    """ ID: 8
        Returns greatest product of multiplying 'n' adjacent digits """
    text = "73167176531330624919225119674426574742355349194934" \
           "96983520312774506326239578318016984801869478851843" \
           "85861560789112949495459501737958331952853208805511" \
           "12540698747158523863050715693290963295227443043557" \
           "66896648950445244523161731856403098711121722383113" \
           "62229893423380308135336276614282806444486645238749" \
           "30358907296290491560440772390713810515859307960866" \
           "70172427121883998797908792274921901699720888093776" \
           "65727333001053367881220235421809751254540594752243" \
           "52584907711670556013604839586446706324415722155397" \
           "53697817977846174064955149290862569321978468622482" \
           "83972241375657056057490261407972968652414535100474" \
           "82166370484403199890008895243450658541227588666881" \
           "16427171479924442928230863465674813919123162824586" \
           "17866458359124566529476545682848912883142607690042" \
           "24219022671055626321111109370544217506941658960408" \
           "07198403850962455444362981230987879927244284909188" \
           "84580156166097919133875499200524063689912560717606" \
           "05886116467109405077541002256983155200055935729725" \
           "71636269561882670428252483600823257530420752963450"
    splits = text.split('0')
    possibles = [_ for _ in splits if len(_) > n-1]
    print(possibles)
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
