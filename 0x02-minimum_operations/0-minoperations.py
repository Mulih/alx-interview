#!/usr/bin/python3
""" Computes minimum operation """


def minOperations(n):
    """
    Method to compute minimum number
    of operations for task Copy All and Paste

    Args:
        n: input value
        factor_list: List to save operations
    Return: Sum of operations

    """
    if n < 2:
        return 0
    factor_list = []
    j = 1
    while n != 1:
        j += 1
        if n % j == 0:
            while n % j == 0:
                n /= j
                factor_list.append(j)
    return sum(factor_list)
