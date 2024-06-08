#!/bin/python3

import sys


def largest_palindrome_product(n):
    max_palindrome = -1
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            product = i * j
            if product < max_palindrome:
                break  # All further products will be smaller
            if product < n and str(product) == str(product)[::-1]:
                max_palindrome = product
    return max_palindrome


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        print(largest_palindrome_product(n))
