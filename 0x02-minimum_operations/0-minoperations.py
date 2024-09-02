#!/usr/bin/python3
"Minimum Operations"


def minOperations(n):
    """ Calculates the fewest number of operations needed to result in
    exactly n 'H' characters in a file."""
    if n <= 1:
        return 0
    # operations = sum(factors)
    operations = 0
    # the smallest prime number
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    return operations
