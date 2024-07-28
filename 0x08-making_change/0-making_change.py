#!/usr/bin/python3
'''make change'''


def makeChange(coins, total):
    """
    Generate changes required to reach total
    Args:
        coins ([List]): [List of Coins available)
        total ([int]): [total amount needed]
    """
    if total <= 0:
        return 0
    check = 0
    temp = 0
    coins.sort(reverse=True)
    for k in coins:
        while check < total:
            check += k
            temp += 1
        if check == total:
            return temp
        check -= k
        temp -= 1
    return -1
