#!/bin/python3

import sys
import math

def largest_prime_factor(n):
    while True:
        p = smallest_prime_factor(n)
        if p < n:
            n //= p
        else:
            return n

# Returns the smallest factor of n, which is in the range [2, n]. The result is always prime.
def smallest_prime_factor(n):
    assert n >= 2
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return i
    return n  # n itself is prime

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        print(largest_prime_factor(n))